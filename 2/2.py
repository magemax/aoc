
z=[]
res0=0
res1=0
with open("input.txt") as maf:
    for line in maf:
        l=line.strip()
        z+=[l.replace("-"," ").replace(":"," ").split()]
        mnn,mxn, c, p = z[-1]
        pb=p
        p="".join(sorted(p))
        mnn=int(mnn)
        mxn=int(mxn)
        if c*mnn in p and c*(mxn+1) not in p:
            res0+=1
        if (pb[mnn-1]==c)^(pb[mxn-1]==c):
            res1+=1
        #print(p,c*mnn, c*(mxn+1), res0)
        #print(pb,(pb[mnn-1]==c)^(pb[mxn-1]!=c), pb[mnn-1], res1)

print("res0 = ", res0)
print("res1 = ", res1)

