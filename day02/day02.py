
from aoc import PuzzleData
import math

puzzle = PuzzleData(__file__)
data = puzzle.getStrList()

RED   = 0
GREEN = 1
BLUE  = 2


class Game ():

    # Game 22: 4 blue; 1 green, 1 red, 16 blue; 15 blue, 1 red

    def __init__(self, game):
        self.game = game

    def getGameID (self) -> int:
        return int(self.game.split(":")[0].split(" ")[1])

    def getDrawCount (self) -> int:
        return self.game.count(";")+1

    def getDraw (self, index: int) -> list[int]:

        colorCount = [0, 0, 0]

        gameInfo = self.game.split(":")[1]               # x red, y green, z blue; k red, l green, m blue
        gameSets = gameInfo.strip().split(";")           # x red, y green, z blue;
        cubes    = gameSets[index].strip().split(",")    
        
        for cube in cubes:
            count, color = cube.strip().split (" ")
            if color == "red":   colorCount[RED]   = int(count)
            if color == "green": colorCount[GREEN] = int(count)
            if color == "blue":  colorCount[BLUE]  = int(count)

        return colorCount


def part1():

    totals = [12, 13, 14]
    possibleGameIDs = 0

    for line in data:

        gamePossible = True

        game = Game (line)
        gameid = game.getGameID()
        ndraws = game.getDrawCount()

        for i in range(ndraws):
            colors = game.getDraw(i)
            if all ([totals[RED] > colors[RED], totals[GREEN] > colors[GREEN], totals[BLUE] > colors[BLUE]]):
                print (f"Game ID {gameid} is not possibe")
                gamePossible = False
                break

        if gamePossible:
            possibleGameIDs += gameid

    print (f"The sum of all possible game IDs is {possibleGameIDs}")



def part2():

    sumPower = 0

    for line in data:

        game = Game (line)
        gameid = game.getGameID()
        ndraws = game.getDrawCount()

        maxColors = [0, 0, 0]

        for i in range (ndraws):
            colors =  game.getDraw(i)
            maxColors[RED]   = max (maxColors[RED],   colors[RED])
            maxColors[GREEN] = max (maxColors[GREEN], colors[GREEN])
            maxColors[BLUE]  = max (maxColors[BLUE],  colors[BLUE])

        power = math.prod(maxColors)
        print (f"Power of game {gameid} = {power}")
        sumPower += power

    print (f"The sum of all game powers is {sumPower}")    


part1()
part2()


