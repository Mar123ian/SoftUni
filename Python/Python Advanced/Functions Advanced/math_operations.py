def math_operations(*args, **kwargs):
    i = 1

    def a(num):
        kwargs["a"] += num

    def s(num):
        kwargs["s"] -= num

    def d(num):
        if num != 0:
            kwargs["d"] /= num

    def m(num):
        kwargs["m"] *= num

    for num in args:
        mapper = {
            1: a,
            2: s,
            3: d,
            4: m
        }
        mapper[i](num)
        i += 1
        if i == 5:
            i = 1
    sorted_output = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    result = ""
    for i in sorted_output:
        result += f"{i[0]}: {i[1]:.1f}\n"

    return (result)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
