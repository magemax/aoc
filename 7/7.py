ss=[]
sp={}
with open("input.txt") as maf:
    for line in maf:
        l=line.strip()
        ss+=[l]

tt=[]
for k in ss:
    z=k.split(" ")
    k1=z[0]+" "+z[1]
    kk={}
    for i in range(4,len(z)-1,4):
        kk[z[i+1]+" "+z[i+2]] = z[i]
    
    sp[k1]=kk


ved=set(["shiny gold"])

r0=0
while True:
    news=0
    for k in sp:
        if k not in ved and any([i in ved for i in sp[k].keys()]):
            ved.add(k)
            news+=1
    r0+=news
    if not news:
        break

print(r0)


from collections import defaultdict

dr1={}
tdr1=defaultdict(int)
while True:
    news=0
    for k in sp:
        if k not in dr1:
            td=[]
            for z in sp[k].keys():
                if z in dr1:
                    tdr1[k]+=(1+dr1[z])*int(sp[k][z])
                    td+=[z]
            for z in td:
                del sp[k][z]
            if (("no" in sp[k].values()) or (not len(sp[k]))):
                dr1[k]=tdr1[k]
                news+=1
    if not news:
        break
print(tdr1["shiny gold"])