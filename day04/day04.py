
from aoc import PuzzleData

import re
from collections import defaultdict

puzzle = PuzzleData(__file__)
data = puzzle.getStrList()

class Card():

    def __init__(self, data: str) -> None:

        self.data = data

        winners = data.split(":")[1].strip().split("|")[0]
        self.winners = re.findall(r"\d+", winners)

        mycards = data.split(":")[1].strip().split("|")[1]
        self.mycards = re.findall(r"\d+", mycards)

    def score(self) -> int:

        score = 0
        for card in self.mycards:
            if card in self.winners:
                if score == 0: score = 1
                else:          score *= 2
        return score

    def nrWinningCards(self) -> int:

        score = 0
        for card in self.mycards:
            if card in self.winners:
                score += 1
        return score

#=======================================

score = 0
totalCards = len(data)
cardCounter: defaultdict[int, int] = defaultdict(lambda:1)

for i in range(len(data)):

    card = Card(data[i])
    nrOfCards = cardCounter[i]

    score += card.score()
    nrWinningCards = card.nrWinningCards()
    
    for j in range(nrWinningCards):
        if i+j+1 < totalCards:
            cardCounter[i+j+1] += nrOfCards


print (f"The winning score is {score}")

sumCards = 0
for i in range(totalCards):
    sumCards+=cardCounter[i]
print (f"The total number of cards is {sumCards}")