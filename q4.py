
class Board:
    
    def __init__(self, table, draws) -> None:
        self.board = table
        self.draws = draws
        self.marked = []
        self.index = 0

    def check_bingo(self) -> bool:
        """check the current board and see if there is a bingo"""
        

    def mark_board(self) -> None:
        """Mark the called value"""
        pass

def initialize_bingo(filename, tracker: list):
    table = []
    with open(filename) as file:
        draws = next(file)  # skip header
        next(file)  # skip empty line
        for line in file:
            line = line.split()
            if line == []:
                tracker.append(Board(table), draws)# store the table to the tracker
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
    initialize_bingo('Q4.txt', tracker)
    while rank == []:
        run_draw(tracker, rank)

