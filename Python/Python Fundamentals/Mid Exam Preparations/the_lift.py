people = int(input())
lift = [int(el) for el in input().split()]

for i in range(len(lift)):

    people_to_add = 4-lift[i] if people >= 4 else people
    people -= people_to_add
    lift[i] += people_to_add

if not people and lift[-1] != 4:
    print("The lift has empty spots!")
if people:
    print(f"There isn't enough space! {people} people in a queue!")
print(*lift)
