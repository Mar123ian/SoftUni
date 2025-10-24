import time


def exec_time(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        stop = time.time()
        result = stop - start
        return result

    return wrapper


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))
