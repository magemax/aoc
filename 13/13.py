ls=[]
with open("input.txt") as maf:
    for line in maf:
        l=line.strip()
        ls+=[l]

ls[0]=int(ls[0])
ls[1]=[int(k) if k!="x" else k for k in ls[1].split(",")]


l = len(ls[1])


i=ls[0]

r=0
while all([k=="x" or i%k!=0 for k in ls[1]]):
    r+=1
    i+=1
idb=[k for k in range(l) if ls[1][k]!="x" and i%ls[1][k]==0][0]
print("Part 1 :", ls[1][idb]*r)




from functools import reduce

def chinese_remainder(n, a):
    sum=0
    prod=reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n,a):
        p=prod//n_i
        sum += a_i* mul_inv(p, n_i)*p
    return sum % prod

def mul_inv(a, b):
    b0= b
    x0, x1= 0,1
    if b== 1: return 1
    while a>1 :
        q=a// b
        a, b= b, a%b
        x0, x1=x1 -q *x0, x0
    if x1<0 : x1+= b0
    return x1
    
n=[k for k in ls[1] if k!='x']
a=[(ls[1][i]-i)%ls[1][i] for i in range(l) if ls[1][i]!="x"]

print("Part 2 : ", chinese_remainder(n,a))



#Version plus lente mais faite artisanalement

k=a[0]
cn=n[0]

for i in range(1,len(n)):
    while k%n[i]!=a[i]:
        k+=cn
    cn*=n[i]
    k%=cn

print("Part 2 bis : ", k)