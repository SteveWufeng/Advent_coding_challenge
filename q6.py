class pool:
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
        new_fishes = dict()
        for cycle in self.__fishes:
            # if the cycle is at 0
            if cycle == 0:
                # reset these 
                new_fishes[6] = self.__fishes[0]
                # add a new gen of fishes
                new_fishes[8] = self.__fishes[0]
            else:
                