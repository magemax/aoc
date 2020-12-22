from time import time

st=time()

ls=[]
with open("input.txt") as maf:
    for line in maf:
        l=line.strip()
        ls+=[l]

canbe= {}

poss=set()
canabe= {}

ing=[]
for i in ls:
    ings, als=i.split("(")
    ings=ings[:-1]
    for j in ings.split(" "):
        poss.add(j)
    ncb=set(ings.split(" "))
    algs=als[:-1].replace("contains ", "contain, ").split(", ")[1:]
    for z in algs:
        if z not in canbe:
            canbe[z]=set(ncb)
        else:
            canbe[z]&=ncb
    ing+=[(set(ings.split(" ")),set(algs))]

p2=set(poss)

from collections import defaultdict

d0={}

p0=set()
for a,i in canbe.items():
    p0|=i
r0=0

"""
variablequinarienavoir=None
for i in ing:
    if "peanuts" in i[1]:
        if variablequinarienavoir is None:
            variablequinarienavoir=i[0]
        else:
            variablequinarienavoir&=i[0]"""
        

wasok=set()
for i in ing:
    for j in i[0]:
        if j not in p0:
            wasok.add(j)
            r0+=1
print("Part 1:", r0)



are={}
arepassif={}
while canbe:
    for i in canbe:
        if len(canbe[i])==1:
            who=i
            break
    are[who]=list(canbe[who])[0]
    arepassif[are[who]]=who
    del canbe[who]
    for i in canbe:
        canbe[i]=set([k for k in canbe[i] if k!=are[who]])

print("Part2 :", ",".join([are[k] for k in sorted(list(are.keys()))]))
print(f"Elapsed : {time()-st:.2f}")