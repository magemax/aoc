from time import time
from collections import defaultdict
st=time()

ls=[]
with open("input.txt") as maf:
    for line in maf:
        l=line.strip()
        ls+=[l]

n=len(ls)
m=len(ls[0])

ss=set()
ssp2 = set()

for i in range(n):
    for j in range(m):
        if ls[i][j]=="#":
            ss.add((i,j,0))
            ssp2.add((i,j,0,0))

def nbs(x,y,z,t=None):
    r=[]
    for xx in range(x-1,x+2):
        for yy in range(y-1,y+2):
            for zz in range(z-1,z+2):
                if t is None:
                    if (x,y,z)!=(xx,yy,zz):
                        r+=[(xx,yy,zz)]
                else:
                    for tt in range(t-1,t+2):
                        if (x,y,z,t)!=(xx,yy,zz,tt):
                            r+=[(xx,yy,zz,tt)]
    return r


def nspart1(ss):
    ss2=set()
    for i in ss:
        mynbs=nbs(*i)
        for j in mynbs + [i]:
            mynnbs=nbs(*j)
            ssj=1 if j in ss else 0
            nbo=sum([1 if x in ss else 0 for x in mynnbs])
            if ssj and nbo in [2,3]:
                ss2.add(j)
            elif ssj==0 and nbo==3:
                ss2.add(j)
    return ss2



#print(len(ss), ss)
for loop in range(6):
    ss=nspart1(ss)
print("Part 1 :", len(ss))


#print(len(ssp2), ssp2)
for loop in range(6):
    ssp2=nspart1(ssp2)
print("Part 2", len(ssp2))


print(f"Elapsed : {time()-st:.2f}")