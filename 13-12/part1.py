import helper
import ast


def compare(a, b):
    if type(a) == type(b) == int:
        return a - b

    if type(a) == int:
        a = [a]
    elif type(b) == int:
        b = [b]
    for i, j in zip(a, b):
        compared = compare(i, j)
        if compared != 0:
            return compared

    if len(a) > len(b):
        return 1
    elif len(b) > len(a):
        return -1
    else:
        return 0


pairs = helper.read_inp("input.txt", sep="\n\n")
pairs = [i.split() for i in pairs]
pairs = [list(map(ast.literal_eval, pair)) for pair in pairs]

s = 0
for index, pair in enumerate(pairs):
    if compare(pair[0], pair[1]) <= 0:
        s += index + 1

print(s)
