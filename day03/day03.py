
from aoc import PuzzleData
from aoc_utils import DataGrid
import math


puzzle = PuzzleData(__file__)
data = DataGrid (puzzle.getStrGrid())

xmax, ymax = data.dim()
coordinates: list[tuple] = []


def extactLeft (data: DataGrid, x: int, y: int, input: str) -> str:

    try: value = data.get(x-1,y)
    except: return input

    x-=1
    if value.isnumeric():
        coordinates.append((x,y))
        result = value + input
        return extactLeft(data, x, y, result)
    
    return input


def extactRight (data: DataGrid, x: int, y: int, input: str) -> str:

    try: value = data.get(x+1,y)
    except: return input

    x+=1
    if value.isnumeric():
        coordinates.append((x,y))
        result = input+value
        return extactRight(data, x, y, result)
    
    return input


def extractNr (data: DataGrid, x: int, y: int) -> int:

    # The value at x, y in data is a number.
    # Find the full number by search for neigbours in x direction.
    result = data.get(x,y)
    coordinates.append((x,y))

    result = extactLeft(data, x, y, result)
    result = extactRight(data, x, y, result)

    return int(result)


def searchValidNrs(data: DataGrid, x: int, y: int):

    numbers = []
    sumNumbers = 0
    gearRatio = 0

    # Search for nrs adjecent to the data point
    # The nrs only run horizontal, but can be attached diagonal.
    for p in [x-1,x,x+1]:
        for q in [y-1,y,y+1]:
            if p == x and q == y: continue
            if (p,q) in coordinates: continue
            try:
                if data.get(p,q).isnumeric():
                    numbers.append (extractNr(data, p, q))
            except: pass

    if len(numbers) == 2: gearRatio = math.prod(numbers)
    sumNumbers = sum(numbers)

    return sumNumbers, gearRatio


partNumbers = 0
gearNumbers = 0

for x in range(xmax):
    for y in range(ymax):
        value = data.get(x,y) 
        if not value in "1234567890.":
            s, g = searchValidNrs(data, x, y)
            partNumbers += s
            gearNumbers += g

print (partNumbers)
print (gearNumbers)