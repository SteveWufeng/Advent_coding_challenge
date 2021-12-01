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

def main():
    filename = 'Q1'
    answer = count_measurements_of_increase(filename)
    print(answer)

if __name__ == '__main__':
    main()


