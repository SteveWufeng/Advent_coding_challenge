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

def binary_search(max, min, cords):
    if max == min:  # base case
        return max

    mid = min + (max-min)//2
    mid_small = min + (mid//2)
    mid_large = mid + (mid//2)

    # find the total fuel for mid
    total_fuel_mid = 0
    total_fuel_small = 0
    total_fuel_large = 0 
    for cord in cords:
        cord = int(cord)
        total_fuel_mid += abs(cord-mid) # find the difference from the cord to our mid
        total_fuel_small += abs(cord-mid_small) # also check the left
        total_fuel_large += abs(cord-mid_large) # and the right

    # determine which way to move(binary search)
    if total_fuel_small <= total_fuel_mid:    # if the smaller side uses less fuel
        return binary_search(mid_small, min, cords) # run binary search again using the small side
    elif total_fuel_large <= total_fuel_mid:    # if the bigger side uses less fuel
        return binary_search(max, mid_large, cords) # run binary search on the big side
    else:
        return mid

def main():
    filename = 'sample.txt'
    max, min, cords = initialize(filename)
    # print(max, min, cords)
    answer = binary_search(max, min, cords)
    print(answer)

if __name__ == '__main__':
    main()