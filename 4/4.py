
p=[]
cp={}
with open("input.txt") as maf:
    for line in maf:
        l=line.strip()
        if l=="":
            p+=[cp]
            cp={}
        else:
            ll=line.split()
            for k in ll:
                a,b=k.split(":")
                cp[a]=b
    if (len(cp)): 
        p+=[cp]
ra=0
r0=0

for a in p:
    isok=True
    isokra=True
    t = "byr","iyr","eyr","hgt","hcl","ecl","pid"
    print(a)
    ra+=1 if len(a) else 0
    for n in t:
        if n not in a:
            if isokra:
                ra-=1
                isokra=False
            isok=False
        else:
            if n=="byr":
                if len(a[n])==4 and "2002">=a[n]>="1920":
                    pass
                else:
                    isok=False
            if n=="iyr":
                if len(a[n])==4 and "2020">=a[n]>="2010":
                    pass
                else:
                    isok=False
            if n=="eyr":
                if len(a[n])==4 and "2030">=a[n]>="2020":
                    pass
                else:
                    isok=False
            if n=="hgt":
                if "cm"==a[n][-2:] and len(a[n])==5 and "193cm">=a[n]>="150cm":
                    pass
                elif "in"==a[n][-2:] and len(a[n])==4 and "76in">=a[n]>="59in":
                    pass
                else:
                    isok=False
            if n=="hcl":
                if len(a[n])==7 and a[n][0]=="#" and all(k in "abcdef0123456789" for k in a[n][1:]):
                    pass
                else:
                    isok=False
            if n=="ecl":
                if a[n] not in ("amb","blu","brn","gry","grn","hzl","oth"):
                    isok=False
            if n=="hcl":
                if len(a[n])==7 and a[n][0]=="#" and all(k in "abcdef0123456789" for k in a[n][1:]):
                    pass
                else:
                    isok=False
            if n=="pid":
                if len(a[n])==9 and all("0"<=k<="9" for k in a[n]):
                    pass
                else:
                    isok=False
    if isok:
        r0+=1
print(ra)
print(r0)