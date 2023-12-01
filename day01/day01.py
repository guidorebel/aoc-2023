
from aoc import PuzzleData

puzzle: PuzzleData = PuzzleData(__file__)
data: list[str] = puzzle.getStrList()

words:  list[str] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits: list[str] = ["1","2","3","4","5","6","7","8","9"]

FROMSTART = 1
FROMEND   = 2

def findDigit(line:str, fromStartorEnd: int) -> int:

    if fromStartorEnd == FROMSTART:
        start = 0
        stop = len(line)
        step = 1

    elif fromStartorEnd == FROMEND:
        start = len(line)-1
        stop = -1
        step = -1

    for index in range(start, stop, step):

        for digit in digits:
            if line[index].find(digit) == 0:
                return int(digit)
            
        if not PARTONE:
            for word in words:
                if line[index::].find(word) == 0:
                    return int(digits[words.index(word)])
    
    return -1


total: int
firstdigit: int
lastdigit: int

#===================

PARTONE = True
total = 0
for line in data:
    firstdigit = findDigit(line, FROMSTART)
    lastdigit  = findDigit(line, FROMEND)
    total += firstdigit * 10 + lastdigit
print (total)

#===================

PARTONE = False
total = 0
for line in data:
    firstdigit = findDigit(line, FROMSTART)
    lastdigit  = findDigit(line, FROMEND)
    total += firstdigit * 10 + lastdigit
print (total)

#===================
