energy = int(input())
won = 0
counter = 0
while True:
    command = input()
    if command == "End of battle":
        print(f"Won battles: {won}. Energy left: {energy}")
        break
    distance = int(command)

    if distance <= energy:
        won += 1
        energy -= distance
        counter += 1
        if counter % 3 == 0:
            energy += won
    else:
        print(
            f"Not enough energy! Game ends with {won} won battles and {energy} energy")
        break

