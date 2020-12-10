instructions=[]
with open("input.txt") as maf:
    for line in maf:
        l=line.strip().split(" ")
        instructions+=[[l[0], int(l[1])]]


def next(pointeur, accu, instructions):
    if instructions[pointeur][0]=="acc":
        accu+=instructions[pointeur][1]
        pointeur+=1
    elif instructions[pointeur][0]=="jmp":
        pointeur+=instructions[pointeur][1]
    elif instructions[pointeur][0]=="nop":
        pointeur+=1
    return pointeur, accu

def part1day8(instructions, depart=0, accubase=0):  #process until visit twice
    res = accubase
    pointeur = depart
    ja=set()
    while True:
        if (pointeur in ja):
            break
        ja.add(pointeur)
        pointeur, res  = next(pointeur, res, instructions)
    print("process until twice done, res =", res)
    return res


def part2day8(instructions):
    N=len(instructions)
    for error in range(N):
        ja=set()
        accu = 0
        pointeur = 0
        if instructions[error][0]=='jmp':
            instructions[error][0]='nop'
        elif instructions[error][0]=="nop":
            instructions[error][0]='jmp'
        while True:
            if (pointeur in ja):  #means we are in infinite loop^
                break
            ja.add(pointeur)
            if pointeur==N:
                print("found the error, res =", accu)
                return accu
            pointeur, accu = next(pointeur, accu, instructions)
        if instructions[error][0]=='jmp':
            instructions[error][0]='nop'
        elif instructions[error][0]=="nop":
            instructions[error][0]='jmp'
    return None



print(part1day8(instructions))
print(part2day8(instructions))