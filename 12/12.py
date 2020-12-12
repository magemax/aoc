ls=[]
with open("input.txt") as maf:
    for line in maf:
        l=line.strip()
        ls+=[[l[0],int(l[1:])]]


pos=(0,0)
cd=0


d= {
    "N":(0,1),
    "S":(0,-1),
    "E":(1,0),
    "W":(-1,0)
}

dirs=[(1,0),(0,-1),(-1,0),(0,1)]

for i in ls:
    if i[0] in d:
        pos=(pos[0]+d[i[0]][0]*i[1],pos[1]+d[i[0]][1]*i[1])
    else:
        if i[0]=="F":
            pos=(pos[0]+dirs[cd][0]*i[1],pos[1]+dirs[cd][1]*i[1])
        if i[0]=="R":
            tt=i[1]//90
            cd=(cd+tt)%4
        if i[0]=="L":
            tt=i[1]//90
            cd=(cd-tt)%4
print("Part 1 :", abs(pos[0])+abs(pos[1]))



pos=0
wp=(10,1)
d= {
    "N":(0,1),
    "S":(0,-1),
    "E":(1,0),
    "W":(-1,0)
}

dirs=[(1,0),(0,-1),(-1,0),(0,1)]

dwp=0

cw=10+1j

for i in ls:
    wps=[wp, (wp[1],-wp[0]), (-wp[0],-wp[1]), (-wp[1],wp[0])]
    if i[0] in d:
        cw+=d[i[0]][0]*i[1]+d[i[0]][1]*i[1]*1j
    else:
        if i[0]=="F":
            pos+=i[1]*cw
        if i[0]=="R":
            tt=i[1]//90
            cw=cw*((-1j)**tt)
        if i[0]=="L":
            tt=i[1]//90
            cw=cw*((1j)**tt)
print("Part 2 :", int(abs(pos.real) + abs(pos.imag)))