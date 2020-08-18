from functools import wraps
from time import time


def timed(func):

    @wraps(func)
    def wrapper(*args):
        t = time()
        res = func(*args)
        runtime = time() - t
        print(f"Finished {func.__name__!r} in {runtime:.12f} secs")
        return res

    return wrapper


def process_list(data: list, power=2):
    return [pow(v, power) for v in data]


def prime(n):
    if n < 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


@timed
def filter_list(numbers, value_type):
    if value_type == 'even':
        return list(filter(lambda n: n % 2 == 0, numbers))
    elif value_type == 'odd':
        return list(filter(lambda n: n % 2 != 0, numbers))
    return list(filter(prime, numbers))


FILTER_BY = ['even', 'odd', 'prime']


def main():
    print('Power function with default power:', process_list([1, 4, 32, 7, 1000]))
    print('Power function with predefined power:', process_list([1, 4, 32, 7, 1000], 8))
    print('Filter list by evens:', filter_list([1, 2, 3, 4, 398], FILTER_BY[0]))
    print('Filter list by odds:', filter_list([1, 2, 3, 4, 398], FILTER_BY[1]))
    print('Filter list by primes:', filter_list([1, 2, 3, 4, 398], FILTER_BY[2]))


if __name__ == "__main__":
    main()
