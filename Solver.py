
def fill_board(bo):

    empty = find_empty(bo)

    if empty is None:
        return True

    row, col = empty

    for k in range(1, 10):

        if check_valid(bo, empty, k):
            bo[row][col] = k
            if fill_board(bo):

                return True
            bo[row][col] = 0

    return False


def check_valid(bo, coord, val):



        # Check column
    for i in range(len(bo)):
        if bo[i][coord[1]] == val and coord[0] != i:
            return False

        # Check row
    for i in range(len(bo[0])):
        if bo[coord[0]][i] == val and coord[1] != i:
            return False

        # Check box
    box_x = coord[1] // 3
    box_y = coord[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == val and (i, j) != coord:
                return False

    return True


def find_empty(bo):
    """
    finds an empty space on the board
    :param bo: partially completed board
    :return: (int, int) row, col
    """

    for x in range(len(bo)):
        for y in range(len(bo[0])):
            if bo[y][x] == 0:
                return y, x
    return None


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0:
            print("--------------------------------", end='')
            print()
        for j in range(len(bo[i])):
            if j % 3 == 0:
                print(" |", end='')
            print(bo[j][i], " ", end='')

        print()
    print("--------------------------------", end='')
    print()


board = [[0, 4, 0, 8, 0, 5, 2, 0, 0],
         [0, 2, 0, 0, 4, 0, 0, 5, 0], 
         [5, 0, 0, 0, 0, 0, 0, 0, 4], 
         [0, 9, 0, 0, 0, 3, 1, 2, 0], 
         [1, 0, 6, 0, 7, 8, 0, 0, 3], 
         [3, 7, 0, 9, 0, 4, 0, 8, 0],
         [0, 0, 0, 0, 0, 6, 7, 0, 0], 
         [0, 0, 8, 3, 5, 9, 0, 1, 0], 
         [0, 1, 9, 0, 0, 7, 6, 0, 0]]

'''board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]'''


fill_board(board)

for i in board:
    print(i)
print(board)

[[6, 4, 1, 8, 3, 5, 2, 7, 9],
 [9, 2, 3, 6, 4, 1, 8, 5, 7],
 [5, 8, 7, 1, 9, 2, 3, 6, 4],
 [4, 9, 5, 7, 6, 3, 1, 2, 8],
 [1, 5, 6, 2, 7, 8, 9, 4, 3],
 [3, 7, 2, 9, 1, 4, 5, 8, 6],
 [2, 3, 4, 5, 8, 6, 7, 9, 1],
 [7, 6, 8, 3, 5, 9, 4, 1, 2],
 [8, 1, 9, 4, 2, 7, 6, 3, 5]]
