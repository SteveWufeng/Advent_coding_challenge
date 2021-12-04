class PowerConsumption:
    __slots__ = ['__input', '__track_digit', '__gama_rate', '__epsilon_rate']
    def __init__(self, filename) -> None:
        self.__input = filename
        self.__track_digit = dict()
        self.__gama_rate, self.__epsilon_rate = self.__compute_input()
    
    def get_power_consumption(self):
        print(self.__gama_rate, self.__epsilon_rate)
        return int(self.__gama_rate, 2) * int(self.__epsilon_rate, 2)

    def __compute_input(self):
        line_count = 0  # this count will be useful for later calculation
        with open(self.__input) as bin_file:
            for binary in bin_file:
                line_count += 1
                for digit in range(len(binary)):
                    # initialize the tracking board
                    if digit not in self.__track_digit and (len(self.__track_digit) < len(binary)-1):
                        self.__track_digit[digit] = 0
                    # check if the value on the digit is one
                    if binary[digit] == '1':
                        self.__track_digit[digit] += 1   # add 1 if yes
        # now that we have counted all 1s in the each column
        # we can now generate gamma
        gamma_rate = ''
        epsilon_rate = ''
        for digit in self.__track_digit:
            ones = self.__track_digit[digit]
            zeros = line_count - ones
            if ones > zeros:
                gamma_rate += '1'
                epsilon_rate += '0'
            elif zeros > ones:
                gamma_rate += '0'
                epsilon_rate += '1'
        return gamma_rate, epsilon_rate
            


def main():
    PC_one = PowerConsumption('sample.txt')
    print(PC_one.get_power_consumption())

if __name__ == '__main__':
    main()