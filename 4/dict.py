dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}


def gennewdict(dict):
    newdict = {}
    for k, v in dict.items():
        if v >= 3:
            newdict[k] = v
    return newdict


print(gennewdict(dict))