def is_safe(board, row, col, N):
    # Check if a queen can be placed at board[row][col]

    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queen_util(board, col, N):
    # Base case: If all queens are placed, return True
    if col >= N:
        return True

    # Try placing a queen in all rows of the current column
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place the queen at board[i][col]
            board[i][col] = 1

            # Recursively place queens in the remaining columns
            if solve_n_queen_util(board, col + 1, N):
                return True

            # If placing the queen doesn't lead to a solution, backtrack
            board[i][col] = 0

    # If no queen can be placed in the current column, return False
    return False


def solve_n_queen(N):
    # Create an empty NxN chessboard
    board = [[0] * N for _ in range(N)]

    if not solve_n_queen_util(board, 0, N):
        print("No solution exists.")
    else:
        print("A solution exists.")
        # Print the board
        for row in board:
            print(row)


# Test the function
N = 4
solve_n_queen(N)
