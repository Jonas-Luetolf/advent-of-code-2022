import helper
import numpy as np

data = helper.read_inp("input.txt")
data = np.array([list(map(int, list(i))) for i in data])

m = 0
for y in range(0, data.shape[0]):
    for x in range(0, data.shape[1]):
        s = 1
        for view in [
            list(data[:y, x]),
            list(data[y + 1 :, x])[::-1],
            list(data[y, :x]),
            list(data[y, x + 1 :])[::-1],
        ]:
            dis = 0
            for i in view:
                if i >= data[y, x]:
                    break
                dis += 1
            if dis == len(view):
                m += 1
                break

print(m)
