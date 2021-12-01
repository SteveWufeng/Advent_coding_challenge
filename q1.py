"""
Question 1
The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:

199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
In this example, there are 7 measurements that are larger than the previous measurement.
"""

def count_measurements_of_increase(filename: str) -> int:
    previous = None
    increased_count = 0
    with open(filename) as input_report:
        for value in input_report:
            value = int(value)
            # compare the current value to the previous value
            if previous:
                if value > previous:
                    increased_count += 1
            previous = value
        return increased_count

"""
Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.

In the above example, the sum of each three-measurement window is as follows:

A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)
In this example, there are 5 sums that are larger than the previous sum.

Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?
"""

def count_measurements_of_increase_windows(filename: str, windows_size=3) -> int:
    previous_sum = None
    increased_count = 0
    windows = []
    with open(filename) as input_report:
        for value in input_report:
            # set up the windows
            value = int(value)
            windows.append(value)
            # compare the current value to the previous value
            if len(windows) == windows_size:
                current_sum = sum(windows)
                if previous_sum != None and previous_sum < current_sum:
                    increased_count += 1
                previous_sum = current_sum
            # if the windows does not have enough elements, we do not dequeue an element
                windows.pop(0)
        return increased_count

def main():
    filename = 'Q1'
    answer = count_measurements_of_increase(filename)
    print(answer)

    filename = 'Q1_part2_sample.txt'
    answer = count_measurements_of_increase_windows(filename)
    print(answer)

if __name__ == '__main__':
    main()


