from copy import deepcopy

rows, cols = [int(el) for el in input().split()]
col_i = cols - 1
matrix = []
b_indexes = []

for row in range(rows):
    row_content = list(input())
    matrix.append(row_content)
    for i in range(len(row_content)):
        if row_content[i] == "P":
            player_column = i
            player_row = row
        if row_content[i] == "B":
            b_indexes.append([row, i])
commands = list(input())


def bunnies():
    is_end = []
    curr_b_indexes = deepcopy(b_indexes)
    for b_row, b_col in curr_b_indexes:

        if b_row != 0:

            if matrix[b_row - 1][b_col] != "P":

                matrix[b_row - 1][b_col] = "B"
                if [b_row - 1, b_col] not in b_indexes:
                    b_indexes.append([b_row - 1, b_col])
            else:
                matrix[b_row - 1][b_col] = "B"
                is_end = [b_row - 1, b_col]

        if b_row != len(matrix) - 1:

            if matrix[b_row + 1][b_col] != "P":

                matrix[b_row + 1][b_col] = "B"
                if [b_row + 1, b_col] not in b_indexes:
                    b_indexes.append([b_row + 1, b_col])
            else:
                matrix[b_row + 1][b_col] = "B"
                is_end = [b_row + 1, b_col]
        if b_col != 0:

            if matrix[b_row][b_col - 1] != "P":

                matrix[b_row][b_col - 1] = "B"
                if [b_row, b_col - 1] not in b_indexes:
                    b_indexes.append([b_row, b_col - 1])
            else:
                matrix[b_row][b_col - 1] = "B"
                is_end = [b_row, b_col - 1]
        if b_col != col_i:

            if matrix[b_row][b_col + 1] != "P":

                matrix[b_row][b_col + 1] = "B"
                if [b_row, b_col + 1] not in b_indexes:
                    b_indexes.append([b_row, b_col + 1])
            else:
                matrix[b_row][b_col + 1] = "B"
                is_end = [b_row, b_col + 1]
    if is_end:
        loss(is_end[0], is_end[1], check=False)


def up(player_row, player_column):
    matrix[player_row][player_column] = "."
    if player_row != 0:
        if matrix[player_row - 1][player_column] != "B":
            player_row, player_column = player_row - 1, player_column
            matrix[player_row][player_column] = "P"
            bunnies()
            return player_row, player_column
        else:
            loss(player_row - 1, player_column, check=True)
    else:
        win(player_row, player_column)


def down(player_row, player_column):
    matrix[player_row][player_column] = "."
    if player_row != len(matrix) - 1:
        if matrix[player_row + 1][player_column] != "B":
            player_row, player_column = player_row + 1, player_column
            matrix[player_row][player_column] = "P"
            bunnies()
            return player_row, player_column
        else:
            loss(player_row + 1, player_column, check=True)
    else:
        win(player_row, player_column)


def left(player_row, player_column):
    matrix[player_row][player_column] = "."
    if player_column != 0:
        if matrix[player_row][player_column - 1] != "B":
            player_row, player_column = player_row, player_column - 1
            matrix[player_row][player_column] = "P"
            bunnies()
            return player_row, player_column
        else:
            loss(player_row, player_column - 1, check=True)
    else:
        win(player_row, player_column)


def right(player_row, player_column):
    matrix[player_row][player_column] = "."
    if player_column != col_i:
        if matrix[player_row][player_column + 1] != "B":
            player_row, player_column = player_row, player_column + 1
            matrix[player_row][player_column] = "P"
            bunnies()
            return player_row, player_column
        else:
            loss(player_row, player_column + 1, check=True)
    else:
        win(player_row, player_column)


def loss(player_row, player_column, check):
    if check:
        bunnies()
    for i in matrix:
        print(*i, sep="")
    print(f"dead: {player_row} {player_column}")
    exit()


def win(player_row, player_column):
    bunnies()
    for i in matrix:
        print(*i, sep="")
    print(f"won: {player_row} {player_column}")
    exit()


for command in commands:
    map = {
        "U": up,
        "D": down,
        "L": left,
        "R": right
    }

    player_row, player_column = map[command](player_row, player_column)
