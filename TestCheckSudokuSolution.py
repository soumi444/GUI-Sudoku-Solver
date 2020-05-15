from CheckSudokuSolution import isValid

def main():
    grid= readASolution()

    if isValid(grid):
        print("Is Valid")
    else:
        print("Is Invalid")

def readASolution():
    print("Enter a Sudoku puzzle solution:")
    grid = []
    for i in range(9):
        line = input().strip().split()
        grid.append([eval(x) for x in line])
    return grid

main()
