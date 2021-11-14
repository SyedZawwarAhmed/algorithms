def input_matrix(no_of_rows, no_of_columns):
    matrix = []
    for i in range(no_of_rows):
        row = []
        for j in range(no_of_columns):
            x = float(input(f"Enter value of at {i+1}{j+1}:- " ))
            row.append(x)
        matrix.append(row)
    return matrix


def display_matrix(matrix):
    for item in matrix:
        for number in item:
            print("{:>8.3f}".format(number), end="   ")
        print()


def get_pivot_element():
    r = int(input("Enter the row number of the pivot element:- "))
    c = int(input("Enter the column number of the pivot element:- "))
    return [r - 1, c - 1]


def make_pivot_one(matrix, pivot_row, pivot_column):
    pivot = matrix[pivot_row][pivot_column]
    for i in range(len(matrix[pivot_row])):
        number = matrix[pivot_row][i]
        matrix[pivot_row][i] = number / pivot
    return matrix

def make_pivot_column_zero(matrix, pivot_row_index):
    pivot_row = matrix[pivot_row_index]
    for i in range(len(matrix)):
        if i != pivot_row_index:
            row = matrix[i] 
            for j in range(len(row)):
                number = row[j]
                row[j] = number + number*pivot_row[j]*-1
    return matrix

matrix = input_matrix(int(input("Enter number of rows:- ")), int(input("Enter number of columns:- ")))

while True:
    inpu = input("If you want to countinue, type (Y/y), else type anything else:- ")
    if inpu == "y" or inpu == "Y":
        pivot_element = get_pivot_element()
        pivot_row = pivot_element[0]
        pivot_column = pivot_element[1]
        matrix = make_pivot_one(matrix, pivot_row, pivot_column)
        matrix = make_pivot_column_zero(matrix, pivot_row)
        display_matrix(matrix)
    else:
        break