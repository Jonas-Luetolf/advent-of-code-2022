import helper

data = helper.read_inp("input.txt")


T = [0, 0]
H = [0, 0]
pos = [str([0, 0])]


for step in data:
    d, l = step.split(" ")
    for i in range(int(l)):
        if d == "U":
            H[0] -= 1
        elif d == "D":
            H[0] += 1
        elif d == "R":
            H[1] += 1
        elif d == "L":
            H[1] -= 1

        if d == "U" and (H[0] + 1) < (T[0]):
            T = [H[0] + 1, H[1]]

        elif d == "D" and (H[0] - 1) > (T[0]):
            T = [H[0] - 1, H[1]]

        elif d == "R" and (H[1] - 1) > (T[1]):
            T = [H[0], H[1] - 1]

        elif d == "L" and (H[1] + 1) < (T[1]):
            T = [H[0], H[1] + 1]

        pos.append(str(T))


print(len(set(pos)))
