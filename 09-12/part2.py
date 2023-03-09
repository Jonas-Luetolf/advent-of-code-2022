import helper

data = helper.read_inp("input.txt")


def follow(hy, hx, ty, tx):
    if abs(hy - ty) == 2 and abs(hx - tx) == 2:
        return [(hy + ty) // 2, (hx + tx) // 2]

    if abs(hy - ty) == 2:
        return [(ty + hy) // 2, hx]

    elif abs(hx - tx) == 2:
        return [hy, (tx + hx) // 2]

    else:
        return [ty, tx]


r = [[0, 0] for _ in range(10)]
res = {str([0, 0])}


for step in data:
    d, l = step.split(" ")
    for _ in range(int(l)):
        if d == "U":
            r[0][0] -= 1
        elif d == "D":
            r[0][0] += 1
        elif d == "R":
            r[0][1] += 1
        elif d == "L":
            r[0][1] -= 1

        prev = r[0]
        for i in range(1, len(r)):
            r[i] = follow(prev[0], prev[1], r[i][0], r[i][1])
            prev = r[i]

        res.add(str(r[-1]))


print(len(res))
