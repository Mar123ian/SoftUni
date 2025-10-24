def is_prime(el):
    if el in [1, 0] or el < 0:
        return False
    for i in range(2, el):
        if el % i == 0:
            return False
    return True


def get_primes(lst):
    for el in lst:

        if is_prime(el):
            yield el


print(list(get_primes([-2, 4, 3, 5, 6, 9, 1, 0])))
