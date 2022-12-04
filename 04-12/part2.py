import helper
import re

data=helper.read_inp("input.txt")
data=[re.split(",|-",i) for i in data]
data=[list(map(int, i)) for i in data]

s=0
for i in data:
    if ((i[1]>=i[2]) and (i[0]<=i[3])) or ((i[3]>=i[0]) and (i[2]<=i[1])): s+=1

print(s)
