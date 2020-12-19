from time import time

st=time()

ls=[]
with open("input.txt") as maf:
    for line in maf:
        l=line.strip()
        ls+=[l]


r=0
r2=0

def reval(s): #Eval function for part 1
    if "(" in s:
        fs=min([k for k in range(len(s)) if s[k]=="("])
        zz=fs
        hm=0
        while fs<len(s):
            hm+= (1 if s[fs]=="(" else (-1 if s[fs]==")" else 0))
            if hm==0:
                break
            fs+=1
        en = fs
        return reval( s[:zz] + str(reval(s[zz+1:en])) + s[en+1:])
    else:
        l = s.split(" ")
        if len(l)<=2:
            return eval(l[0])
        else:
            return reval(str(eval("".join(l[:3]))) + " " + " ".join(l[3:]))


def reval2(s): #Eval function for part 2
    if "(" in s:
        fs=min([k for k in range(len(s)) if s[k]=="("])
        zz=fs
        hm=0
        while fs<len(s):
            hm+= (1 if s[fs]=="(" else (-1 if s[fs]==")" else 0))
            if hm==0:
                break
            fs+=1
        en = fs
        return reval2( s[:zz] + str(reval2(s[zz+1:en])) + s[en+1:])
    if "+" in s:
        l = s.split(" ")
        fs=min([k for k in range(len(l)) if l[k]=="+"])
        zz=fs-1
        en = fs + 2 
        return reval2( ((" ".join(l[:zz])  +" ") if zz else "")+ str(eval("".join(l[zz:en]))) + ((" " + " ".join(l[en:])) if en<len(l) else ""))
    else:
        l = s.split(" ")
        if len(l)<=2:
            return str(eval(l[0]))
        else:
            return reval2(str(eval("".join(l[:3]))) + " " + " ".join(l[3:]))

for k in ls:
    ev2=reval2(k)
    ev=reval(k)
    print(k, "=", ev, "(ou", ev2, ")")
    r+=ev
    r2+=int(ev2)

    
print("Part 1", r)
print("Part 2", r2)



print(f"Elapsed : {time()-st:.2f}")