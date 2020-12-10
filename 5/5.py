ss=[]
with open("input.txt") as maf:
    for line in maf:
        l=line.strip()
        ss+=[l]
mxx=0
t=[0]*10000

for k in ss:
    b=k[:7].replace("F","0").replace("B","1")
    c=k[7:].replace("L","0").replace("R","1")
    print(b+c)
    mxx=max(mxx, int(b+c,2))
    print(int(b+c,2))
    t[int(b+c,2)]+=1
print(mxx)

for i in range(1,9999):
    if t[i-1] and t[i+1] and not t[i]:
        print("posres=", i)


