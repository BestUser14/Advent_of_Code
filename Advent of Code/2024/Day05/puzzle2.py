import math
a = open("input.txt", 'r')
rules={}
toggle=0
pages=[]
while(line:=a.readline()):
    line = line.strip('\n')
    if '|' not in line:
        toggle=1
    if toggle:
        pages.append(line.split(','))
    else:
        if line.split('|')[0] in rules.keys():
            rules[line.split('|')[0]].append(line.split('|')[1])
        else:
            rules[line.split('|')[0]]=[(line.split('|')[1])]
pages=pages[1:]

def check(listy, rules):
    for i in range(len(listy)):
        for z in range(len(listy[:i])):
            if listy[:i][z] in rules.keys():
                if listy[:i][z] in rules[listy[i]]:
                    return 0
    return 1
def fix(listy,rules):
    while not check(listy,rules):
        for i in range(len(listy)):
            for z in range(len(listy[:i+1])):
                if listy[i-z] in rules.keys():
                    if listy[i-z] in rules[listy[i]]:
                        item=listy.pop(i-z)
                        listy.append(item)
                        z-=1
    return listy

def handler(listy,rules):
    if not check(listy,rules):
        return int(fix(listy,rules)[math.floor(len(listy)/2)])
    return 0
summ=0
for x in range(len(pages)):
    summ+=handler(pages[x],rules)
print(summ)
