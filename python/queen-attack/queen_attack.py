class Queen:
    def __init__(self, row, column):
        # handle errors if queen is out of bounds
        if row < 0:
            raise ValueError("row not positive")
        elif row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        elif column > 7:
            raise ValueError("column not on board")

        self.row = row
        self.col = column

    def can_attack(self, another_queen):
        # handle queens on overlapping position
        if self.row == another_queen.row and self.col == another_queen.col:
            raise ValueError("Invalid queen position: both queens in the same square")
        
        # obtain attack information
        row_diff = abs(self.row - another_queen.row)
        col_diff = abs(self.col - another_queen.col)

        return row_diff == 0 or col_diff == 0 or row_diff == col_diff