import helper

data=helper.read_inp("input.txt")
res=[20,60,100,140,180,220]
x=1
s=0
cycles=0

for i in data:
    try:
        func,attribut=i.split(" ")
    except:
        func="noop"

    if func=="noop":
        cycles+=1

    else:
        x=x+int(attribut)
        cycles+=2

    if (func=="noop" and cycles in res):
        s+=cycles*x

    elif (func=="addx" and ((cycles-1 in res) or (cycles in res))):
        if cycles in res:
            s+=(cycles)*(x-int(attribut))
        else:
            s+=(cycles-1)*(x-int(attribut))
        
print(s,x)
