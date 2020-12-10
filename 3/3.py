s=[]
with open("input.txt") as maf:
    for line in maf:
        l=line.strip()
        s+=[l]

r1=1

for slope in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
    res0=0
    for i in range(slope[1]-1,len(s), slope[1]):
        res0+=1 if s[i][(slope[0]*i)%len(s[i])]=="#" else 0
    print(res0)
    r1*=res0

print(r1)