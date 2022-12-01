with open("input.txt","r") as f:
    inp=f.read()

data=inp.split("\n\n")
data=[i.split("\n") for i in data]
sums=[]

for index,i in enumerate(data):
    if "" in i:
        continue

    s=sum([int(j) for j in i])
    sums.append(s)

sums.sort(reverse=True)

print(sum(sums[:3]))
