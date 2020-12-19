from time import time

st=time()

ls=[]
with open("input.txt") as maf:
    for line in maf:
        l=line.strip()
        ls+=[l]


rules={}

words=[]

for l in ls:
    lp = l.split(" ")
    if len(lp)>1:
        lp[0]=lp[0][:-1]    
        for i in range(len(lp)):
            if lp[i]=="|":
                pass
            elif '"' in lp[i]:
                lp[i]= lp[i][1:-1]
            else:
                lp[i]=int(lp[i])
        rules[lp[0]] = lp[1:]
    elif len(lp)==1 and len(lp[0])>1:
        words+=[l]

import re

maxnum=5
def matchw(ruleid, part):
    if part==2:
        if ruleid==8:
            return f"({matchw(42,part)})+"
        if ruleid==11:
            mymaxes= ["("+f"{matchw(42,part)}"*i +f"{matchw(31,part)}" *i +")" for i in range(1,maxnum+1)]
            return f"({'|'.join(mymaxes)})"
    if len(rules[ruleid])==1:
        if isinstance(rules[ruleid][0], int):
            return matchw(rules[ruleid][0],part)
        else:
            return rules[ruleid][0]
    elif len(rules[ruleid])==2:
        return f"({matchw(rules[ruleid][0],part)}{matchw(rules[ruleid][-1],part)})"
    elif len(rules[ruleid])==3:
        if "|" in rules[ruleid]:
            return f"(({matchw(rules[ruleid][0],part)})|({matchw(rules[ruleid][-1],part)}))"
        else:
            return f"({matchw(rules[ruleid][0],part)}{matchw(rules[ruleid][1],part)}{matchw(rules[ruleid][-1],part)})"
    elif len(rules[ruleid])==5:
        return f"(({matchw(rules[ruleid][0],part)}{matchw(rules[ruleid][1],part)})|({matchw(rules[ruleid][-2],part)}{matchw(rules[ruleid][-1],part)}))"
    else:
        raise





#print("to match", "^"+matchw(0)+"$")
for part in [1,2]:
    r0=0
    for k in words:
        matched = re.match("^"+matchw(0, part)+"$",k)
        is_match = bool(matched)
        if (is_match):
            r0+=1

    print("Part",part,":",r0)

print(f"Elapsed : {time()-st:.2f}")