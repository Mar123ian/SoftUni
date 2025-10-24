from collections import deque

strength = [int(el) for el in input().split()]
accuracy = deque([int(el) for el in input().split()])
total_goals = 0
while strength and accuracy:
    strength_value = strength[-1]
    accuracy_value = accuracy[0]
    sum = strength_value + accuracy_value

    if sum == 100:
        strength.pop()
        accuracy.popleft()
        total_goals += 1

    elif sum < 100:
        if strength_value < accuracy_value:
            strength.pop()

        elif strength_value > accuracy_value:
            accuracy.popleft()

        else:
            strength[-1] = sum
            accuracy.popleft()

    else:
        strength[-1] -= 10
        accuracy_to_move = accuracy.popleft()
        accuracy.append(accuracy_to_move)

if total_goals == 3:
    print("Paul scored a hat-trick!")
elif total_goals == 0:
    print("Paul failed to score a single goal.")
elif total_goals > 3:
    print("Paul performed remarkably well!")
elif 0 < total_goals < 3:
    print("Paul failed to make a hat-trick.")

if total_goals:
    print(f"Goals scored: {total_goals}")
if strength:
    print(f"Strength values left: ", end="")
    print(*strength, sep=", ")
if accuracy:
    print(f"Accuracy values left: ", end="")
    print(*accuracy, sep=", ")
