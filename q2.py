"""
Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

forward 5 adds 5 to your horizontal position, a total of 5.
down 5 adds 5 to your depth, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13.
up 3 decreases your depth by 3, resulting in a value of 2.
down 8 adds 8 to your depth, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15.
After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?
"""
# def analyse_command(command) -> int:
    


def get_final_x_y(filename):
    x, y = 0, 0 # initialize cordinate
    with open(filename) as file:
        for line in file:
            command = line.split()
            # analyse command
            direction = command[0].lower()
            move_value = int(command[1])

            # perform command action
            if direction == 'forward':
                x += move_value
            elif direction == 'down':
                y -= move_value
            else:
                y += move_value
    return x, y

def main():
    # x, y = get_final_x_y('Q2.txt')
    x, y = get_final_x_y('sample.txt')
    print(x*y)

if __name__ == '__main__':
    main()
            

 