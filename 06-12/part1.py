import helper

data = helper.read_inp("input.txt")[0]
s = 0
for i in range((len(data) - 4)):
    if 4 == len(set(list(data[i : i + 4]))):
        s = i + 4
        break

print(s)
