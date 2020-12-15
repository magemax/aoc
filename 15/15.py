ls=[20,9,11,0,1,2] #input


n=len(ls)

a={}
for k in range(n-1):
    a[ls[k]]=k

values=[2020,30000000]
k=n
pv=ls[-1]
mv=max(values)
nv=0
while k<mv:
    if (pv in a):
        npv=k-1-a[pv]
        a[pv]=k-1
        pv=npv
    else:
        a[pv]=k-1
        pv=0
    k+=1
    ls+=[pv]
    if k==values[nv]:
        print("Part",nv+1,":",ls[-1])
        nv+=1
