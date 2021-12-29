
def read_cordinate_all(x1, y1, x2, y2) -> set:
    """return a list of cordinate from point 1 to point2""" 
    change_y = False
    change_x = False
    # check which one is changing
    if x1 == x2:
        changing = [y1, y2]
        change_y = True
    elif y1 == y2:
        changing = [x1, x2]
        change_x = True
    else:
        return diagonal_set_of_cord(x1, y1, x2, y2) # run another function if the two cordinates are diagonal
    # start adding the cordinates
    set_of_cord = set()
    # check which one is bigger
    if changing[0] > changing[1]:
        changing[0], changing[1] = changing[1], changing[0]
    # add the cordinates
    for i in range(changing[0], changing[1]+1):
        if change_x:
            set_of_cord.add((i, y1))
        elif change_y:
            set_of_cord.add((x1, i))
    return set_of_cord

def diagonal_set_of_cord(x1, y1, x2, y2) -> set:
    # determine x and y are increasing or not.
    x_increasing = 1    # 1 means that it is increasing
    y_increasing = 1    # -1 means that it is decreasing
    if x2 < x1:
        x_increasing = -1
        x2 -=2
    if y2 < y1:
        y_increasing = -1
        y2 -=2
    # create cordinate sets
    set_of_cord = set()
    x_val = [i for i in range(x1, x2+1, x_increasing)]
    y_val = [j for j in range(y1, y2+1, y_increasing)]
    for k in range(len(x_val)):
        set_of_cord.add((x_val[k], y_val[k]))
    return set_of_cord

def mark_cordinate(x:int, y:int, grid:dict) -> None:
    """this funciton mark the cordinate on the grid"""
    if (x, y) not in grid:
        grid[(x, y)] = 0
    grid[(x, y)] +=1

def get_points_overlaps(grid:dict) -> int:
    """return number of points >=2"""
    count_overlap_points = 0
    for key in grid:
        if grid[key] >=2:
            count_overlap_points += 1
    return count_overlap_points

def extract_file(filename:str) -> dict:
    """return a grid by extracting the file"""
    grid = dict()
    with open(filename) as file:
        for line in file:
            line = line.split(' -> ')
            point1 = line[0]
            point1 = point1.split(',')

            point2 = line[1]
            point2 = point2.split(',')
            point1[0], point1[1], point2[0], point2[1] = int(point1[0]), int(point1[1]), int(point2[0]), int(point2[1])
            set_cords = read_cordinate_all(point1[0], point1[1], point2[0], point2[1])
            if set_cords:
                for point in set_cords:
                    mark_cordinate(point[0], point[1], grid)
    return grid
            
def main():
    # grid = extract_file('sample.txt')
    grid = extract_file('q5.txt')
    answer = get_points_overlaps(grid)
    print(answer)

if __name__ == '__main__':
    main()