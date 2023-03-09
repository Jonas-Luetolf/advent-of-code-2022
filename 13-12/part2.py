import ast
import functools


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


with open("input.txt", "r") as f:
    packages = f.read().replace("\n\n", "\n").strip().split()

packages = list(map(ast.literal_eval, packages))
packages.extend(([[2]], [[6]]))


packages.sort(key=functools.cmp_to_key(compare))
print((packages.index([[2]]) + 1) * (packages.index([[6]]) + 1))
