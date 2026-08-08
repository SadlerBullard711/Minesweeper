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
        #number of rows and columns must be equal and greater than 1.
        self.size = 10
        for row in range(self.size):
            new_column = []
            self.board.append(new_column)
            for column in range(self.size):
                new_cell = Cell()
                self.board[row].append(new_cell)

        #add mines to the board.
        #mines is the number of currently placed mines.
        mines = 0
        mines_max = len(self.board[0]) * len(self.board[0])
        #mines_num is the number of mines to place.
        mines_num = 1
        #if the set number of mines is greater than spaces on the board, shrink the number of mines.
        if mines_num > mines_max:
            mines_num = mines_max
        for row in range(len(self.board[row]) - 1):
            for column in range(len(self.board[row]) - 1):
                #place mines until reaching mines_num
                while mines < mines_num:
                    row_num = random.randint(0, len(self.board[row]) - 1)
                    col_num = random.randint(0, len(self.board[row]) - 1)
                    coordinate = [row_num, col_num]
                    #reroll the coordinate if there is already a mine there.
                    while coordinate in self.mine_list:
                        row_num = random.randint(0, len(self.board[row]) - 1)
                        col_num = random.randint(0, len(self.board[row]) - 1)
                        coordinate = [row_num, col_num]
                    #add to the number of placed mines.
                    mines += 1
                    #subtract from the number of unrevealed safe spaces, as the space is no longer safe.
                    self.unrevealed -= 1
                    #set the cell to be a mine.
                    self.board[row_num][col_num].mine = True
                    #update the mine list so mines are not placed on that spot again.
                    self.mine_list.append(coordinate)
                    #add the mine to the cell.number of adjacent cells.
                    if (coordinate[0] != 0) and (coordinate[1] != 0):
                        top_left = self.board[coordinate[0] - 1][coordinate[1] - 1]
                        top_left.add_number()
                    if (coordinate[0] != 0) and (coordinate[1] != self.size - 1):
                        top_right = self.board[coordinate[0] - 1][coordinate[1] + 1]
                        top_right.add_number()
                    if (coordinate[0] != 0):
                        top_middle = self.board[coordinate[0] - 1][coordinate[1]]
                        top_middle.add_number()
                    if (coordinate[0] != self.size - 1) and (coordinate[1] != 0):
                        bottom_left = self.board[coordinate[0] + 1][coordinate[1] - 1]
                        bottom_left.add_number()
                    if (coordinate[0] != self.size - 1) and (coordinate[1] != self.size -1):
                        bottom_right = self.board[coordinate[0] + 1][coordinate[1] + 1]
                        bottom_right.add_number()
                    if (coordinate[0] != self.size - 1):
                        bottom_middle = self.board[coordinate[0] + 1][coordinate[1]]
                        bottom_middle.add_number()
                    if (coordinate[1] != 0):
                        middle_left = self.board[coordinate[0]][coordinate[1] - 1]
                        middle_left.add_number()
                    if (coordinate[1] != self.size - 1):
                        middle_right = self.board[coordinate[0]][coordinate[1] + 1]
                        middle_right.add_number()
 


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
                elif cell.flagged:
                    new_row += "|?|  "
                #If cell in not revealed or flagged, show nothing.
                else:
                    new_row += "| |  "
            print("")
            print(new_row)


class Cell:
    def __init__(self):
        self.mine = False
        self.flagged = False
        self.revealed = False
        self.number = 0

    def reveal(self, board: Board):
        board.unrevealed -= 1
        self.revealed = True
        print(board.unrevealed)

    def toggle_flag(self):
        self.flagged = not self.flagged

    def add_number(self):
        self.number += 1