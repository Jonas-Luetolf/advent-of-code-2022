with open("input.txt","r") as f:
    inp=f.read()

data=inp.split("\n\n")
data=[i.split("\n") for i in data]
max_sum=(0,0)

for index,i in enumerate(data):
    if "" in i:
        continue

    s=sum([int(j) for j in i])
    if max_sum[0]<s:
        max_sum=(s,(index+1))

print(max_sum[0])
