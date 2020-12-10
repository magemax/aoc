ll=[]
with open("input.txt") as maf:
    for line in maf:
        l=line.strip()
        ll+=[l]
ll+=[""]

r0=0
r1=0
cr=set()
cr1=None
for k in ll:
    print(k,":")
    if len(k)==0:
        print(cr,cr1)
        r0+=len(cr)
        if  cr1!=set("?"):
            r1+=len(cr1)
        cr=set()
        cr1=None
        print(r0,r1)
        print()
    else:
        cr2=set()
        for i in k:
            cr.add(i)
            cr2.add(i)
        if cr1 is None:
            cr1=cr2
        else:
            cr1=cr1&cr2
        print(cr,cr1)

print(r0)  
print(r1)