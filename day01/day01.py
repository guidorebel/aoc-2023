
from aoc import PuzzleData

puzzle: PuzzleData = PuzzleData(__file__)
data: list[str] = puzzle.getStrList()

words:  list[str] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits: list[str] = ["1","2","3","4","5","6","7","8","9"]


def findDigit(line:str, fromStart: bool, searchWords: bool) -> int:

    if fromStart: r = range(len(line))
    else:         r = range(len(line))[::-1]

    for index in r:

        for digit in digits:
            if line[index].find(digit) == 0:
                return int(digit)
            
        if searchWords:
            for word in words:
                if line[index::].find(word) == 0:
                    return int(digits[words.index(word)])
    
    return -1


total: int
firstdigit: int
lastdigit: int

# Part 1
#===================

total = 0
for line in data:
    firstdigit = findDigit(line, True, False)
    lastdigit  = findDigit(line, False, False)
    total += firstdigit * 10 + lastdigit
print (total)


# Part 2
#===================

total = 0
for line in data:
    firstdigit = findDigit(line, True, True)
    lastdigit  = findDigit(line, False, True)
    total += firstdigit * 10 + lastdigit
print (total)
