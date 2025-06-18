num = int(input())
odd = set()
even = set()

for i in range(1, num+1):
    name_nums = [ord(letter) for letter in input()]
    name_sum = sum(name_nums)//i

    if name_sum & 1 == 0:
        even.add(name_sum)
    else:
        odd.add(name_sum)

if (odd_sum := sum(odd)) == (even_sum := sum(even)):
    print(*(odd | even), sep=", ")

elif odd_sum > even_sum:
    print(*(odd-even), sep=", ")

elif odd_sum < even_sum:
    print(*(odd ^ even), sep=", ")
