presents, size = int(input()), int(input())
matrix = []
nice = 0
nice_p = 0
end = False

for row in range(size):
    row_content = input().split()
    matrix.append(row_content)
    for i in range(size):
        if row_content[i] == "S":
            santa_column, santa_row = i, row
        if row_content[i] == "V":
            nice += 1
            nice_p += 1


def no_presents():
    for i in matrix:
        print(*i)
    print(f"No presents for {nice} nice kid/s.")


def good_job():
    for i in matrix:
        print(*i)
    print(f"Good job, Santa! {nice_p} happy nice kid/s.")


def out_of_presents():
    global end

    if nice > 0:
        print("Santa ran out of presents!")
        no_presents()
    else:
        good_job()
    end = True


def good_kid():
    global presents
    global nice
    global end

    presents -= 1
    nice -= 1
    if presents == 0:
        out_of_presents()


def bad_kid():
    global presents
    global nice
    global end

    presents -= 1

    if presents == 0:
        out_of_presents()


def happy_santa(santa_row, santa_column):
    global presents
    global nice
    global end

    up = matrix[santa_row - 1][santa_column]
    down = matrix[santa_row + 1][santa_column]
    right = matrix[santa_row][santa_column + 1]
    left = matrix[santa_row][santa_column - 1]

    around_santa = [up, down, right, left]

    matrix[santa_row - 1][santa_column] = "-"
    matrix[santa_row + 1][santa_column] = "-"
    matrix[santa_row][santa_column + 1] = "-"
    matrix[santa_row][santa_column - 1] = "-"

    for el in around_santa:
        if el == "X" and not end:
            bad_kid()

        elif el == "V" and not end:
            good_kid()


def check(event, santa_row, santa_column):
    global presents
    global nice

    if event == "V":
        good_kid()
    elif event == "C":
        happy_santa(santa_row, santa_column)


def up(santa_row, santa_column):
    if santa_row != 0:
        matrix[santa_row][santa_column] = "-"
        santa_row, santa_column = santa_row - 1, santa_column
        event = matrix[santa_row][santa_column]
        matrix[santa_row][santa_column] = "S"

        check(event, santa_row, santa_column)
    return santa_row, santa_column


def down(santa_row, santa_column):
    if santa_row != size - 1:
        matrix[santa_row][santa_column] = "-"
        santa_row, santa_column = santa_row + 1, santa_column
        event = matrix[santa_row][santa_column]
        matrix[santa_row][santa_column] = "S"

        check(event, santa_row, santa_column)
    return santa_row, santa_column


def left(santa_row, santa_column):
    if santa_column != 0:
        matrix[santa_row][santa_column] = "-"
        santa_row, santa_column = santa_row, santa_column - 1
        event = matrix[santa_row][santa_column]
        matrix[santa_row][santa_column] = "S"

        check(event, santa_row, santa_column)
    return santa_row, santa_column


def right(santa_row, santa_column):
    if santa_column != size - 1:
        matrix[santa_row][santa_column] = "-"
        santa_row, santa_column = santa_row, santa_column + 1
        event = matrix[santa_row][santa_column]
        matrix[santa_row][santa_column] = "S"

        check(event, santa_row, santa_column)
    return santa_row, santa_column


while True and not end:
    command = input()
    if command == "Christmas morning":
        break
    map = {
        "up": up,
        "down": down,
        "left": left,
        "right": right
    }

    santa_row, santa_column = map[command](santa_row, santa_column)

if not end:
    if nice == 0:
        good_job()
    else:
        no_presents()
