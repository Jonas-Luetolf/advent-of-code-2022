import helper

data=helper.read_inp("input.txt")
res=[(["." for x in range(0,40)]) for y in range(0,6)]
x=1
s=0
cycles=240

data_i=0

instr_cycles=0
instr=""

for i in range(1,cycles+1):
    if instr_cycles==0:
        instr=data[data_i]
        data_i+=1

        if instr=="noop": instr_cycles=1
        else: instr_cycles=2

    instr_cycles-=1

    if x - 1 <= ((i - 1) % 40) <= x + 1:
        res[((i - 1) // 40)][((i - 1) % 40)]="#"



    if instr_cycles == 0:
            if instr.startswith('addx '):
                _, n_s = instr.split()
                x += int(n_s)



for i in res:
    print("".join(i))
