import random

class Board:
    #Create the board and set the unrevealed safe cells total and list of mines.
    def __init__(self):
        #mine_list keeps track of mine coordinates.
        self.mine_list = []
        #unrevealed keeps track of how many unrevealed cells are left.
        self.unrevealed = 0
        #board is the board itself, a list of lists of cells.
        self.board = []
        for row in range(10):
            new_column = []
            self.board.append(new_column)
            for column in range(10):
                new_cell = Cell()
                self.board[row].append(new_cell)

        #add mines to the board.
        mines = 0
        for row in range(10):
            for column in range(10):
                #stop adding mines after specific number.
                while mines < 20:
                    row_num = random.randint(0, 9)
                    col_num = random.randint(0, 9)
                    coordinate = [row_num, col_num]
                    if coordinate in self.mine_list:
                        row_num = random.randint(0, 9)
                        col_num = random.randint(0, 9)
                        coordinate = [row_num, col_num]
                    mines += 1
                    self.board[row_num][col_num].mine = True


    def draw_board(self):
        print("      0    1    2    3    4    5    6    7    8    9   ")
        
        #For each row in the column, show each cell.
        for row in range(len(self.board)):
            new_row = f"{row}|   "
            for column in range(len(self.board[row])):
                cell = self.board[column][row]
                #If the cell is revealed, show the number or mine.
                if cell.revealed:
                    if cell.mine:
                        new_row += "|X|  "
                    else:
                        new_row += f"|{cell.number}|  "
                #If the cell is flagged, show a flag (?)
                elif cell.flag:
                    new_row += "|(?)|  "
                #If cell in not revealed or flagged, show nothing.
                else:
                    new_row += "| |  "
            print("")
            print(new_row)
                



class Cell:
    def __init__(self, mine = False, flag = False, revealed = False, number = 0):
        self.mine = mine
        self.flag = flag
        self.revealed = revealed
        self.number = number


board = Board()
board.draw_board()