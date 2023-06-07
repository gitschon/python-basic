numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]


def findnumb(num):
    if num > 50 and num % 2 == 0:
        return True
    return False


print(list(filter(findnumb, numbers)))
