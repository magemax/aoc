from time import time

st=time()

ls=[]
with open("input.txt") as maf:
    for line in maf:
        l=line.strip()
        ls+=[l]


m=0
poss=[] #contient les intervalles où chaque catégorie
posses=None #posses[i][j] = nombre d'indices situés en i-ième position d'un ticket valides pour la catégorie j
toget=[]
r=0
idl=0
nbcool=0
mt=None
for k in ls:
    ks=k.split()
    if len(ks)>=4:
        a,b=[int(i) for i in ks[-3].split("-")]
        c,d=[int(i) for i in ks[-1].split("-")]
        poss+=[[(a,b),(c,d)]]
        if k[:5]=="depar":
            toget+=[idl]
    if k=="your ticket:":
        m=1
    if m==1 and "," in k:
        a=[int(i) for i in k.split(",")]
        if mt is None:
            mt=a[:]
        if posses is None:
            posses=[[0 for i in range(len(poss))] for j in range(len(poss))]
        ii=0
        wik=set()
        igok=True
        for i in a:
            isok=False
            kk=0
            for p in poss:
                if p[0][0]<=i<=p[0][1] or p[1][0]<=i<=p[1][1]:
                    isok=True
                    wik.add((kk,ii))
                kk+=1
            if not isok:
                igok=False
                r+=i
            ii+=1
        if igok:
            nbcool+=1
            for p in wik:
                posses[p[1]][p[0]]+=1
            
    idl+=1

print("part 1:",r)

toattr=list(range(len(posses[0])))
res={}
rr=1
jadone=set()
while toattr:
    kk=0
    diff=0
    for k in posses:
        if kk not in jadone:
            if nbcool in k:
                zz=[i for i in range(len(k)) if k[i]==nbcool]
                kzz=[i for i in toattr if i in zz]
                if len(kzz)==1:
                    res[kzz[0]]=kk
                    jadone.add(kk)
                    toattr=[j for j in toattr if j!=kzz[0]]
                    if kzz[0] in toget:
                        rr*=mt[kk]
                    diff=1
        kk+=1
    if not diff:
        break

print("Part 2:",rr)
print(f"Elapsed : {time()-st:.2f}")