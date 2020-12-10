ss=[]
with open("input.txt") as maf:
    for line in maf:
        l=line.strip()
        ss+=[int(l)]


for k in range(25,len(ss)):
    isok=False
    for i in range(max(0,k-25),k):
        for j in range(i+1,k):
            if ss[k]==ss[i]+ss[j]:
                isok=True
                break
    if not isok:
        print("P1 OK", ss[k])
        break


i=0
i2=0
where=k
target=ss[k]

k=0

while i2<where:
    if k<target:
        k+=ss[i2]
        i2+=1
    elif k>target:
        k-=ss[i]
        i+=1
    else:
        print("P2 OK", min(ss[i:i2])+ max(ss[i:i2]))
        break