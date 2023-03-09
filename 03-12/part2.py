import helper


def isdublicate(l1, l2, l3):
    for i in l1:
        for j in l2:
            for k in l3:
                if i == j == k:
                    return i
    return None


def adjust(c):
    if c >= 97:
        return c - 96
    else:
        return c - 38


data = helper.read_inp("input.txt")
dublicates = []

for i in range(2, len(data), 3):
    dublicates.append(isdublicate(data[i - 2], data[i - 1], data[i]))

dublicates = map(adjust, list(map(ord, dublicates)))
print(sum(dublicates))
