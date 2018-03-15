class Board:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = self.create_empty_grid()
        self.pieces = []
        self.targets = []

    def create_empty_grid(self):
        grid = []
        for r in range(self.rows):
            grid.append([])
            for c in range(self.cols):
                grid[r].append(0)
        return grid

    def print_grid(self):
        print("    ", end='')
        for c in range(self.cols):
            print(str(c), "   ", end='')
        print("\n")
        for r in range(self.rows):
            print(str(r), "   ", end='')
            for c in range(self.cols):
                print(str(self.grid[r][c]), "   ", end='')
            print("\n")


test_board = Board(9, 5)
test_board.print_grid()
