class Pool:
    __slots__ = ['__fishes', '__day_past']
    def __init__(self) -> None:
        self.__fishes = dict()
        self.__day_past = 0

        # initialize keys in the fish dict
        for cycle in range(0, 9):
            self.__fishes[cycle] = 0

    def add_fish(self, state):
        # add the fish to the pool
        self.__fishes[state] += 1
    
    def past_one_day(self):
        # create a new pool
        new_fishes = dict()
        # initialize the new pool
        for cycle in range(0, 9):
            new_fishes[cycle] = 0

        for cycle in self.__fishes:
            # if the cycle is at 0
            if cycle == 0:
                # reset these 
                new_fishes[6] += self.__fishes[0]
                # add a new gen of fishes
                new_fishes[8] += self.__fishes[0]
            else:
                # reduce fishes cycle by one
                new_fishes[cycle-1] += self.__fishes[cycle]
        # update day passed & current pool
        self.__fishes = new_fishes
        self.__day_past += 1

    def count_fish(self) -> int:
        """this funciton is for reading all the fishes in the pool"""
        count = 0
        for key in self.__fishes:
            count += self.__fishes[key]

        return count

def read_file(filename) -> Pool:
    with open(filename) as file:
        # read the first line
        line = next(file)
        # split the first line in commas
        line = line.split(',')
        new_pool = Pool()
        for fish in line:
            new_pool.add_fish(int(fish))
        return new_pool

def main():
    # filename = 'sample.txt'
    filename = 'q6.txt'
    pool = read_file(filename)
    for _ in range(256):
        pool.past_one_day()
    count = pool.count_fish()
    print(count)

if __name__ == '__main__':
    main()