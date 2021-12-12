
class Board:
    
    def __init__(self, table, draws) -> None:
        self.board = table
        self.draws = draws
        self.marked = []
        self.index = 0
        self.bingo = False

    def check_bingo(self) -> bool:
        """check the current board and see if there is a bingo"""
        if self.bingo == True:  # if the table has already been checked return True to save resource
            return True

        # check horizontally
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] not in self.marked:
                    break
                if j == len(self.board[i])-1:
                    self.bingo = True
                    return True
            
        # check verticle
        for i in range(len(self.board[0])):
            for j in range(len(self.board)):
                if self.board[i][j] not in self.marked:
                    break
                if j == len(self.board)-1:
                    self.bingo = True
                    return True
        
        return False    # return false if neither loop found a bingo.

    def mark_board(self) -> None:
        """Mark the called value"""
        draw_val = self.draws[self.index]
        self.index += 1
        for row in self.board:
            if draw_val in row:
                self.marked.append(draw_val)
                return
        

def initialize_bingo(filename, tracker: list):
    table = []
    with open(filename) as file:
        draws = next(file)  # skip header
        draws = draws.split(',')
        next(file)  # skip empty line
        for line in file:
            line = line.split()
            if line == []:
                tracker.append(Board(table, draws))# store the table to the tracker
                table = []                  # reset and start a new table if the line is empty
            else:
                table.append(line)          # else just store the row to the current table.

def run_draw(tracker: list, rank: list):
    for i in range(len(tracker)):
        table = tracker[i]
        table.mark_board()
        bingo = table.check_bingo()
        if bingo and (not (i in rank)):
            rank.append(i)
        

def main():
    rank = []
    tracker = list()
    initialize_bingo('sample.txt', tracker)
    while rank == []:
        run_draw(tracker, rank)
    print('table:', rank[0])
    for row in tracker[rank[0]].board:
        print(row)
    print()
    print(tracker[rank[0]].marked)

if __name__ == '__main__':
    main()
