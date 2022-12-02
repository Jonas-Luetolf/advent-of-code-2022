import helper

data=helper.read_inp("input.txt",)
data=[i.split(" ") for i in data]

points={"X":0,"Y":3,"Z":6,"AX":3,"BX":1,"CX":2,"AY":1,"BY":2,"CY":3,"AZ":2,"BZ":3,"CZ":1}
s=0

for i in data:
    s+=points[i[1]]
    if "".join(i) in points:
        s+=points["".join(i)]

print(s)
