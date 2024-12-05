import math
a = open("input.txt", 'r')
rules={}
toggle=0
pages=[]
while(line:=a.readline()):
    line = line.strip('\n')
    if line=="":
        toggle=1
    if toggle:
        pages.append(line.split(','))
    else:
        if line.split('|')[0] in rules.keys():
            rules[line.split('|')[0]].append(line.split('|')[1])
        else:
            rules[line.split('|')[0]]=list(line.split('|')[1])
pages=pages[1:]

def check(listy, rules):
    for i in range(len(listy)):
        for z in range(len(listy[:i+1])):
            if listy[i-z] in rules.keys():
                if listy[i-z] in rules[listy[i]]:
                    return 0
    return listy[math.floor(len(listy)/2)]

summ=0
for x in range(len(pages)):
    summ+=int(check(pages[x],rules))
print(summ)
