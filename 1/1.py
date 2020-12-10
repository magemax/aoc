a=[]
with open("input.txt") as maf:
    for line in maf:
        a+=[int(line.strip())]

a=sorted(a)
print(len(a))
for i2 in range(len(a)):
    print(i2)
    target=2020-a[i2]
    i0=i2+1
    i1=len(a)-1
    while i0<i1:
        if (a[i0]+a[i1]==target):
            print(i0,i1,a[i0],a[i1],a[i2],a[i0]*a[i1]*a[i2])
            break
        elif a[i0]+a[i1]<target:
            i0+=1
        else:
            i1-=1
