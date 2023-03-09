import helper


def isdublicate(l1, l2):
    for i in l1:
        for j in l2:
            if i == j:
                return i
    return None


def adjust(c):
    if c >= 97:
        return c - 96
    else:
        return c - 38


data = helper.read_inp("input.txt")
dublicates = []
for i in data:
    dublicates.append(isdublicate(i[: int(len(i) / 2)], i[int(len(i) / 2) :]))

dublicates = map(adjust, list(map(ord, dublicates)))
print(sum(dublicates))
