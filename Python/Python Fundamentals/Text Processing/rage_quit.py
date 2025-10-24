def add_word(text):
    n = " "
    t = ""

    for el in text:
        if el.isnumeric():
            if t[len(t) - 1] != "|":
                t += "|"
            n += el
        else:
            if n[len(n) - 1] != "|":
                n += "|"
            t += el
    n = n.split("|")
    t = t.split("|")
    t.remove("")
    n.remove(" ")
    length = len(set(("".join(t)).upper()))
    print(f"Unique symbols used: {length}")
    for i in range(len(t)):
        print((t[i] * int(n[i])).upper(), end="")


text = input()
add_word(text)
