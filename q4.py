
class Board:
    
    def __init__(self, table, draws) -> None:
        self.board = table
        self.draws = draws
        self.index = 0

    def check_bingo(self) -> bool:
        """check the current board and see if there is a bingo"""
        pass

    def mark_board(self, value: str) -> None:
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

def main():
    tracker = list()
    initialize_bingo('Q4.txt', tracker)

