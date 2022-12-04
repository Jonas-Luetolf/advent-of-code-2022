import helper
import re

data=helper.read_inp("input.txt")
data=[re.split(",|-",i) for i in data]
data=[list(map(int, i)) for i in data]

s=0
for i in data:
    if (i[0]<=i[2] and i[1]>=i[3]) or (i[2]<=i[0] and i[3]>=i[1]): s+=1

print(s)
