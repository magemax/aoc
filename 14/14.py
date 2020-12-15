ls=[]
with open("input.txt") as maf:
    for line in maf:
        l=line.strip()
        A=l.split(" = ")
        ls+=[A]


cm="X"*36
mem={}
for l in ls:
    if l[0][:2]=="me":
        w=int(l[0][4:-1])
        what=int(l[1])
        for i in range(36):
            if cm[-1-i]=='0' and what&(1<<i):
                what^=(1<<i)
            if cm[-1-i]=='1' and what&(1<<i)==0:
                what^=(1<<i)
        mem[w]=what
    else:
        cm=l[1]


print("Part 1 :",sum(mem.values()))




cm="X"*36
mem={}
for l in ls:
    if l[0][:2]=="me":
        w=int(l[0][4:-1])
        what=int(l[1])
        ta=[]
        for i in range(36):
            if cm[-1-i]=='1' and w&(1<<i)==0:
                w^=(1<<i)
            if cm[-1-i]=='X':
                ta+=[i]
        for i in range(1<<len(ta)):
            ww=w
            for z in range(len(ta)):
                if i&(1<<z):
                    ww^=(1<<ta[z])
            mem[ww]=what
    else:
        cm=l[1]


print("Part 2 :",sum(mem.values()))