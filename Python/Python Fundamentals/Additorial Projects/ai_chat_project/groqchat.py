from groq import Groq
from colorama import Fore, Back, Style

client = Groq(
    api_key='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',
)
chatnum = 0


def clear():
    with open("data.txt", "r") as f:
        data = (f.readlines())

        for i in range(len(data)):

            if "\n" in data[i]:
                data[i] = "".join(data[i].split("\n"))
        data = list(filter(lambda a: a != "", data))

        data = "\n".join(data)

    with open("data.txt", "w") as f:
        f.write(data)


clear()


def next():
    with open("data.txt", "r") as f:
        data = (f.readlines())
        curr = int("".join(data[-2].split("\n")))
        new_curr = curr + 1
        if new_curr == int(data[-1]) + 1:
            print(Fore.YELLOW + "\nДостигна последния чат!")
            print(Style.RESET_ALL, end="")
            return
        data[-2] = str(new_curr)
        data = "\n".join(data)
    with open("data.txt", "w") as f:
        f.write(data)

    print(Fore.RED + "\nСЛЕДВАЩ ЧАТ:")
    print(Style.RESET_ALL, end="")
    load()


def pr():
    with open("data.txt", "r") as f:
        data = (f.readlines())

        curr = int("".join(data[-2].split("\n")))
        new_curr = curr - 1
        if new_curr == 0:
            print(Fore.YELLOW + "\nДостигна първия чат!")
            print(Style.RESET_ALL, end="")
            return
        data[-2] = str(new_curr)

        data = "\n".join(data)
    with open("data.txt", "w") as f:
        f.write(data)

    print(Fore.RED + "\nПРЕДИШЕН ЧАТ:")
    print(Style.RESET_ALL, end="")
    load()


def new():
    with open("data.txt", "r") as f:
        data = (f.readlines())
        last = int("".join(data[-1].split("\n")))
        new_last = last + 1

        data[-1] = str(new_last)
        lst = int("".join(data[-2].split("\n")))
        new_lst = new_last

        data[-2] = str(new_lst)
        data = "\n".join(data)
    with open("data.txt", "w") as f:
        f.write(data)
    chat = str(new_last) + ".txt"
    with open(chat, "w") as f:
        pass
    print(Fore.RED + "\nНОВ ЧАТ:")
    print(Style.RESET_ALL, end="")
    load()


def load():
    global chatnum
    with open("data.txt", "r") as f:
        data = (f.readlines())
        last_chat = "".join(data[-2].split("\n")) + ".txt"
        chatnum = "".join(data[-2].split("\n"))
    if len(data) > 1:
        with open(last_chat, "r") as f:
            l = f.readlines()
            for li in l:
                if li[0] == "Y":
                    print(Fore.GREEN + li, end="")
                    print(Style.RESET_ALL, end="")
                else:
                    print(li, end="")
    print(Fore.YELLOW + "\n\n•••\nЗа нов чат напиши /нов")
    print("За смяна на модела напиши /модел")
    print("За смяна на чата напиши /п за предишен чат \nили /с за следващ чат\n•••", end="")
    print(Style.RESET_ALL)


def get_model():
    with open("data.txt", "r") as f:
        m = f.readlines()
    return m[0][:-1]


def change_model(choice):
    match choice:
        case 1:
            new_model = "llama3-8b-8192"
        case 2:
            new_model = "gemma2-9b-it"
        case 3:
            new_model = "mixtral-8x7b-32768"
    with open("data.txt", "r") as f:
        d = f.readlines()

        d[0] = (new_model)
        d = "\n".join(d)
    with open("data.txt", "w") as f:
        f.write(d)

    print(Fore.YELLOW + f"Моделът е успешно сменен на {new_model}")
    print(Style.RESET_ALL, end="")


def get_ai_response(user_input):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": user_input}
            ],
            model=get_model(),
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"


load()

while True:
    user_input = input(Fore.GREEN + "\nYou: ")
    print(Style.RESET_ALL, end="")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye! 👋")
        break
    elif user_input.lower() == "/модел":
        print(Fore.YELLOW + "Избери модел")
        print("1. llama3-8b-8192")
        print("2. gemma2-9b-it")
        print("3. mixtral-8x7b-32768")

        choice = int(input("Вашият избор: "))
        print(Style.RESET_ALL, end="")
        change_model(choice)
        continue
    elif user_input.lower() == "/нов":
        new()
        continue
    elif user_input.lower() == "/с":
        next()
        continue
    elif user_input.lower() == "/п":
        pr()
        continue
    response = get_ai_response(user_input)
    with open(chatnum + ".txt", "a") as f:
        f.write("\n\nYou: " + user_input + "\n\nAI: " + response)
    print("\nAI: " + response)
