import sys


def sums():

    digit_string = sys.argv[1]

    res = 0
    for d in digit_string:
        res += int(d)
    return res


if __name__ == "__main__":
    print(sums())
