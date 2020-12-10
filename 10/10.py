ss=[]
with open("input.txt") as maf:
    for line in maf:
        l=line.strip()
        ss+=[int(l)]



a=[0]+sorted(ss)+[max(ss)+3]


c=0

for k in a:
    if k<=c+3:
        c=k
    else:
        print(c+3)
        break


d=[0]*1000000
for k in range(1,len(a)):
    d[a[k]-a[k-1]]+=1

print(d[1]*d[3])

b=[0]*len(a)
b[0]=1

for k in range(1,len(a)):
    i=k-1
    while i>=0 and a[k]>a[i]>=a[k]-3:
        b[k]+=b[i] 
        i-=1
    
print(b[-2])
