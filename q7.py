"""
Idea:
find max and min
use binary search to look for the answer
"""

def initialize(filename): # returns max, min, set of crab's cordinate
    # process cordinate
    with open(filename) as file:
        crab_cords = next(file)             # read the first line
        crab_cords = crab_cords.split(',')  # split with comma
    
    # find max and min
    max = 0
    min = 0
    for cord in crab_cords:
        cord = int(cord)
        if cord > max:
            max = cord
        if cord < min:
            min = cord

    return max, min, crab_cords

def main():
    filename = 'sample.txt'
    max, min, cords = initialize(filename)
    print(max, min, cords)

if __name__ == '__main__':
    main()