from time import time
from math import sqrt

st=time()

ls=[]
with open("input.txt") as maf:
    for line in maf:
        l=line.strip()
        ls+=[l]

#Filling tiles dictionary
nxt=[]
tiles = {}
num=0
for l in ls:
    if l =="":
        tiles[num]=nxt
        nxt=[]
    elif l[:4]=="Tile":
        num=int(l[5:-1])
    else:
        nxt+=[l]

tiles[num]=nxt
nxt=[]




ds={}

#Gets list of signatures for the borders of a tile 
def sigs(tile):
    global ds
    if tile not in ds:
        mastrl="".join([k[0] for k in tiles[tile]][::-1])
        mastru="".join(tiles[tile][0])
        mastrr="".join([k[-1] for k in tiles[tile]])
        mastrd="".join(tiles[tile][-1][::-1])
        ds[tile]=(mastrl, mastru, mastrr, mastrd)
    return ds[tile]


from collections import defaultdict

sig_to_tile_rotation=defaultdict(list) #indexes by signature the tiles and associated rotation

for k in tiles:
    kk=0
    for i in sigs(k):
        sig_to_tile_rotation[i]+=[(k,kk,0)]
        sig_to_tile_rotation["".join(i[::-1])]+=[(k,kk,1)]
        kk+=1

rr=1
lastrr=None
for k in tiles:
    if sorted([len(sig_to_tile_rotation[i]) for i in ds[k]])==[1,1,2,2]: #It's a corner !!!
        rr*=k
        lastrr=rr
print("Part 1:", rr)

correct=list(tiles.keys())[0] #Assuming rotation is correct for an arbitrary tile.

#Rotates a tile :
#flip is 1 if the tile t should be flipped
# cotefrom is the side on which the signature is on the tile t
# coteto is the side it should be on
def rotate(t, flip, cotefrom, coteto):
    global tiles
    global ds
    new_tile=[i[:] for i in tiles[t]]
    if flip: #flips vertically
        new_tile=[i[::-1] for i in new_tile]
        if cotefrom in [0,2]:
            cotefrom=2-cotefrom
    nbrot=(cotefrom-coteto)%4
    for _ in range(nbrot):
        new_tile= ["".join([new_tile[j][-1-i] for j in range(n)]) for i in range(n)]
    tiles[t]=new_tile
    del ds[t]
    sigs(t)


#Setting correct rotation and neighbours for all cells
ved=set([correct])
n=len(tiles[correct])
to_process=[correct]
voisins={k:[None]*4 for k in tiles.keys()}

while to_process:
    new_to_process=[]
    for i in to_process: #gathering unvisited neighbours (very inefficiently)
        for k in range(4):
            for j in tiles:
                for kk in range(4):
                    if j not in ved or (j!=i and voisins[j][kk] is None):
                        if sigs(i)[k]==sigs(j)[kk]:
                            rotate(j, 1, kk, (2+k)%4)
                            ved.add(j)
                            new_to_process+=[j]
                            voisins[i][k]=j
                            voisins[j][(2+k)%4]=i
                            break
                        elif sigs(i)[k]=="".join(sigs(j)[kk][::-1]):
                            rotate(j,0,kk,(2+k)%4)
                            ved.add(j)
                            new_to_process+=[j]
                            voisins[i][k]=j
                            voisins[j][(2+k)%4]=i
                            break          
    to_process=new_to_process



upper_left_corner=None
for i in voisins:
    if voisins[i][0] is None and voisins[i][1] is None:
        upper_left_corner=i

sz=int(sqrt(len(tiles)))

ordered_tiles_index=[[0] * sz for i in range(sz)]



ordered_tiles_index[0][0]=upper_left_corner
for i in range(sz):
    for j in range(sz):
        if j+1<sz and ordered_tiles_index[i][j+1]==0:
            ordered_tiles_index[i][j+1]=voisins[ordered_tiles_index[i][j]][2]
        if i+1<sz and ordered_tiles_index[i+1][j]==0:
            ordered_tiles_index[i+1][j]=voisins[ordered_tiles_index[i][j]][3]
        
img_reconst=[]

for i in range(sz):
    nls= [ "" for ii in range(1,n-1)]
    for j in range(sz):
        nls= [nls[k-1] + tiles[ordered_tiles_index[i][j]][k][1:-1] for k in range(1,n-1)]
    img_reconst+=nls

#Ooououf j'ai mon img_reconst

#rotations of dragons
d1 = [(0,18),(1,0),(1,5),(1,6),(1,11),(1,12),(1,17),(1,18),(1,19),(2,1),(2,4),(2,7),(2,10),(2,13),(2,16)]
d2 = [(0,1),(1,19),(1,14),(1,13),(1,8),(1,7),(1,2),(1,1),(1,0),(2,18),(2,15),(2,12),(2,9),(2,6),(2,3)]
d3 = [(2,18),(1,0),(1,5),(1,6),(1,11),(1,12),(1,17),(1,18),(1,19),(0,1),(0,4),(0,7),(0,10),(0,13),(0,16)]
d4 = [(2,1),(1,19),(1,14),(1,13),(1,8),(1,7),(1,2),(1,1),(1,0),(0,18),(0,15),(0,12),(0,9),(0,6),(0,3)]


totalhash=0
for i in img_reconst:
    for j in i:
        if j=="#":
            totalhash+=1


myrealrealres = []
for dragon in [d1,d2,d3,d4]:
    N=len(img_reconst)
    yadd=set()
    for i in range(N):
        for j in range(N):
            if i+2<N and j+19<N:
                if all(img_reconst[i+k[0]][j+k[1]]=="#" for k in dragon):
                    for k in dragon:
                        yadd.add((i+k[0],j+k[1]))
    myrealrealres+=[totalhash-len(yadd)]

    yadd=set()
    for i in range(N):
        for j in range(N):
            if j+2<N and i+19<N:
                if all(img_reconst[i+k[1]][j+k[0]]=="#" for k in dragon):
                    for k in dragon:
                        yadd.add((i+k[1],j+k[0]))
    myrealrealres+=[totalhash-len(yadd)]



print("Part 2 : ", min(myrealrealres))
print(f"Elapsed : {time()-st:.2f}")