# Put your "check_celebrity" function below this line
def check_celebrity(grid):

    for celebrity_number in range(len(grid)):
        column_total =0
        for row in range(len(grid)):
            column_total += grid[row][celebrity_number]
        row_total = 0
        for column in range(len(grid)):
            row_total += grid[celebrity_number][column]

        if column_total == len(grid) and row_total == 1:
            print("#", celebrity_number, "is a celebrity.")
        else:
            print("#", celebrity_number, "is not a celebrity.")

# The code will test your function

print("Test 1, Should show #2 is a celebrity.")
grid = [ [1, 1, 1, 0],
         [0, 1, 1, 0],
         [0, 0, 1, 0],
         [1, 0, 1, 1] ]

check_celebrity(grid)

print("Test 2, Should show no one is a celebrity.")
grid = [ [1, 1, 1, 0, 1],
         [0, 1, 1, 0, 1],
         [0, 0, 1, 0, 0],
         [1, 0, 0, 1, 1],
         [1, 0, 0, 1, 1] ]

check_celebrity(grid)

print("Test 3, Should show #2 is a celebrity.")
grid = [ [1, 1, 1, 0, 1],
         [0, 1, 1, 0, 1],
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 1],
         [1, 0, 1, 1, 1] ]

check_celebrity(grid)

print("Test 4, Should show no one is a celebrity.")
grid = [ [1, 1, 1, 0, 1],
         [0, 1, 1, 0, 1],
         [1, 0, 1, 0, 0],
         [0, 0, 1, 0, 1],
         [1, 0, 1, 1, 1] ]

check_celebrity(grid)

