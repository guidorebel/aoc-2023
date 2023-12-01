

def manhattan (a: list[int], b: list[int]) -> int:
    
    '''
    Return the manhattan distance between two 2D coordinates
    
    Example:
    input: (2, 7) and (4, 9)
    outut: (4-2) + (9-7) = 4
    '''
    
    assert (len(a) == 2)
    assert (len(b) == 2)
    
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


