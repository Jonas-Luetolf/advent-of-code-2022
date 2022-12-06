import helper

data=helper.read_inp("input.txt")[0]
s=0
for i in range((len(data)-14)):
    if 14==len(set(list(data[i:i+14]))):
        s=i+14
        break

print(s)
