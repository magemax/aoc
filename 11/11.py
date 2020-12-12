ss=[]
with open("input.txt") as maf:
    for line in maf:
        l=line.strip()
        ss+=[l]

n=len(ss)
m=len(ss[0])



#neighbours
def nbs(i,j):
    r=[]
    for z in ((-1,-1),(1,1), (-1,1),(1,-1), (0,1),(0,-1),(1,0),(-1,0)):
        ii=i+z[0]
        jj=j+z[1]
        if (n>ii>=0) and m>jj>=0:
            r+=[(ii,jj)]
    return r

#next step
def nspart1(ss):
    ss2=[[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            nns=nbs(i,j)
            nbo=sum([1 if ss[a][b]=='#' else 0 for (a,b) in nns])
            if ss[i][j]=="L" and nbo==0:
                ss2[i][j]="#"
            elif ss[i][j]=="#" and nbo>=4:
                ss2[i][j]="L"
            else:
                ss2[i][j]=ss[i][j]
    return ss2


kkk=0
css=ss[:]
while True:
    ss2=nspart1(css)
    if ss2==css:
        break
    css=ss2
    kkk+=1

rr=0
for k in css:
    for i in k:
        if i=="#":
            rr+=1

print("Part 1 :", rr)




def nbs2(i,j,ss):
    r=[]
    for z in ((-1,-1),(1,1), (-1,1),(1,-1), (0,1),(0,-1),(1,0),(-1,0)):
        ii=i+z[0]
        jj=j+z[1]
        while (n>ii>=0) and m>jj>=0:
            if ss[ii][jj]!=".":
                r+=[(ii,jj)]
                break
            else:
                ii+=z[0]
                jj+=z[1]
    return r

def nspart2(ss):
    ss2=[[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            nns=nbs2(i,j,ss)
            nbo=sum([1 if ss[a][b]=='#' else 0 for (a,b) in nns])
            if ss[i][j]=="L" and nbo==0:
                ss2[i][j]="#"
            elif ss[i][j]=="#" and nbo>=5:
                ss2[i][j]="L"
            else:
                ss2[i][j]=ss[i][j]
    return ss2


kkk=0
while True:
    ss2=nspart2(ss)
    if ss2==ss:
        break
    ss=ss2
    kkk+=1

rr=0
for k in ss:
    for i in k:
        if i=="#":
            rr+=1

print("Part 2 :", rr)
