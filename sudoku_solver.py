import tkinter as tk

class SudokuGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sudoku Solver")

        self.board = [[tk.StringVar() for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                cell = tk.Entry(self.window, width=4, font=("Arial", 14), textvariable=self.board[i][j])
                cell.grid(row=i+1, column=j+1)
        
        solve_button = tk.Button(self.window, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=11, column=5)

    def solve_sudoku(self):
        puzzle = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                try:
                    puzzle[i][j] = int(self.board[i][j].get())
                except ValueError:
                    puzzle[i][j] = 0
        
        if self.solve(puzzle):
            for i in range(9):
                for j in range(9):
                    self.board[i][j].set(str(puzzle[i][j]))
        else:
            print("No solution exists.")

    def solve(self, puzzle):
        find = self.find_empty(puzzle)
        if not find:
            return True
        else:
            row, col = find

        for num in range(1, 10):
            if self.is_valid(puzzle, num, (row, col)):
                puzzle[row][col] = num

                if self.solve(puzzle):
                    return True

                puzzle[row][col] = 0

        return False

    def is_valid(self, puzzle, num, pos):
        # Check row
        for i in range(len(puzzle[0])):
            if puzzle[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(len(puzzle)):
            if puzzle[i][pos[1]] == num and pos[0] != i:
                return False

        # Check 3x3 box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if puzzle[i][j] == num and (i, j) != pos:
                    return False

        return True

    def find_empty(self, puzzle):
        for i in range(len(puzzle)):
            for j in range(len(puzzle[0])):
                if puzzle[i][j] == 0:
                    return (i, j)
        return None

    def start(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = SudokuGUI()
    gui.start()
