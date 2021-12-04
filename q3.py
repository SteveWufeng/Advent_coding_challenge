from array_queue import Queue


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

class LifeSupportRating:

    def __init__(self, filename) -> None:
        self.input = filename
        self.track = Queue()
        self.index = 0

    def get_oxygen_generator_rating(self):
        self.__initialize_track()       # refill the track
        self.index = 0                  # reset index
        while self.track.size() != 1:   # while the size is down to one
            self.__filter(self.index, 'more')
            self.index += 1
        return repr(self.track)
    
    def get_CO2_scrubber_rating(self):
        self.__initialize_track()       # refill the track
        self.index = 0                  # reset index
        while self.track.size() != 1:   # while the size is down to one
            self.__filter(self.index, 'less')
            self.index += 1
        return repr(self.track)
    
    def __initialize_track(self):
        self.track = Queue()            # reset Queue
        with open(self.input) as file:
            for line in file:
                self.track.enqueue(line)# add item to Queue
    
    def __ones_or_zeros(self, digit, comparator):
        ones_count = 0
        line_count = self.track.size()
        for _ in range(line_count):
            binary = self.track.dequeue().strip()   # take one binary out
            if binary[digit] == '1':
                ones_count += 1             # count the ones in that digit
            self.track.enqueue(binary)      # put the binary back in
        zeros_count = line_count - ones_count

        if comparator == 'more':
            if zeros_count > ones_count:
                return '0'
            elif ones_count >= zeros_count:
                return '1'
        else:
            if zeros_count <= ones_count:
                return '0'
            elif ones_count < zeros_count:
                return '1'

    def __filter(self, digit, comparator):
        most_count = self.__ones_or_zeros(digit, comparator)
        for _ in range(self.track.size()):
            binary = self.track.dequeue()   # take one binary out
            if binary[digit] == most_count:
                self.track.enqueue(binary)  # put the binary to the back if they are what we want.

def main():
    # PC_one = PowerConsumption('sample.txt')
    # PC_one = PowerConsumption('q3.txt')
    # print(PC_one.get_power_consumption())

    # life_support_rating = LifeSupportRating('sample.txt')
    life_support_rating = LifeSupportRating('q3.txt')
    oxygen = life_support_rating.get_oxygen_generator_rating()
    co2 = life_support_rating.get_CO2_scrubber_rating()
    print(oxygen, co2)
    oxygen = int(oxygen, 2)
    co2 = int(co2, 2)
    print(oxygen * co2)

if __name__ == '__main__':
    main() 