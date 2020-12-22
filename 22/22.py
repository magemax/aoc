from time import time

st=time()

ls=[]
with open("input.txt") as maf:
    for line in maf:
        l=line.strip()
        ls+=[l]


a=[]
b=[]
for i in range(1,26):
    a+=[int(ls[i])]
    
for i in range(28,len(ls)):#
    b+=[int(ls[i])]


aa,bb=a[:],b[:]


ii=0
while a and b:
    if a[0]>b[0]:
        a+=[a[0],b[0]]
    else:
        b+=[b[0],a[0]]
    a=a[1:]
    b=b[1:]
    ii+=1


f = lambda x:sum([(len(x)-i)*x[i] for i in range(len(x))])
print("Part 1:",max(f(a),f(b)))
print(f"Elapsed : {time()-st:.2f}")

dd={}

def solverecurs(u,v):
    global dd
    jadone=set()
    tjd=(tuple(u), tuple(v))
    while True:
        tjd=(tuple(u), tuple(v))
        if tjd in jadone:
            dd[tjd]=(0,f(u))
            return dd[tjd]
        jadone.add(tjd)
        if not u:
            return 1,f(v)
        if not v:
            return 0,f(u)
        if len(u)>u[0] and len(v)>v[0]:
            winner=solverecurs(u[1:u[0]+1],v[1:v[0]+1])[0]
            if winner==0:
                u+=[u[0],v[0]]
            else:
                v+=[v[0],u[0]]
        else:
            if u[0]>v[0]:
                u+=[u[0],v[0]]
            else:
                v+=[v[0],u[0]]
        u=u[1:]
        v=v[1:]
    else:
        return dd[tjd]


print("Part 2:",solverecurs(aa,bb)[1])

print(f"Elapsed : {time()-st:.2f}")