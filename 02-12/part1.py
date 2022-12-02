import helper

data=helper.read_inp("input.txt",)
data=[i.split(" ") for i in data]

points={"X":1,"Y":2,"Z":3,"AY":6,"BZ":6,"CX":6,"AX":3,"BY":3,"CZ":3}
s=0

for i in data:
    s+=points[i[1]]
    if "".join(i) in points:
        s+=points["".join(i)]

print(s)
