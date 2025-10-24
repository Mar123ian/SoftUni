n, m = [int(el) for el in input().split(", ")]
coordinates = []
time = 16
map = [list(input()) for i in range(n)]
for el in map:
    if "C" in el:
        coordinates = [map.index(el), el.index("C")]


def check(y, x, defuse=0):
    if 0 <= y < len(map) and 0 <= x < len(map[1]):
        place = map[y][x]
        coordinates[0] = y
        coordinates[1] = x
        if place == "*":
            return
        if defuse:
            time = defuse - 3

            if time >= 0:
                map[y][x] = "D"
                return "defused"
            else:
                map[y][x] = "X"
                return "exploded"
        if place == "B":
            return "to_defuse"
        if place == "T":
            map[y][x] = "*"
            print("Terrorists win!")
            return "dead"
    else:
        return


commands = {}
state = None
while True:
    command = input()
    time -= 1

    y, x = coordinates
    if command == "up":
        state = None
        state = check(y - 1, x)

    elif command == "down":
        state = None
        state = check(y + 1, x)

    elif command == "left":
        state = None
        state = check(y, x - 1)

    elif command == "right":
        state = None
        state = check(y, x + 1)

    elif command == "defuse":
        if state == "to_defuse":
            bomb_result = check(y, x, time)
            if bomb_result == "defused":
                print(f"Counter-terrorist wins!\nBomb has been defused: {time - 3} second/s remaining.")
                break
            else:
                print("Terrorists win!\nBomb was not defused successfully!")
                print(f"Time needed: {abs(time - 3)} second/s.")
                break
        else:
            time -= 1

    if state == "dead":
        break
    if time <= 0:
        print("Terrorists win!\nBomb was not defused successfully!")
        print(f"Time needed: {0} second/s.")
        break

for el in map:
    print("".join(el))
