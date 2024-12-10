import re
f=open("input.txt",'r')
inp=""
while(temp := f.readline()):
    #inp.append(temp)
    inp=inp+temp
f.close()
summ=0
inp=[inp] #ignore the first for loop, i thought all the lines restarted the
#do thing whatver
for itera in range(len(inp)):
    dos=[]
    for i in range(len(inp[itera])):
        if inp[itera][i:i+4]=="do()":
            dos.append([1,i])
        if inp[itera][i:i+7]=="don't()":
            dos.append([0,i])
    a=[[1,0]]
    a.extend(dos)
    a.append([1,len(inp[itera])])
    print(a)
    legit=[]
    for i in range(len(a)-1):
        if a[i][0]:
            legit.extend(re.findall(r"mul\([0-9]+,[0-9]+\)",inp[itera][a[i][1]:a[i+1][1]]))
    #print(legit)

    real_legit=[]
    for x in range(len(legit)):
        real_legit.append(legit[x][4:-1].split(','))
    print(real_legit)

    for y in range(len(real_legit)):
        summ+= int(real_legit[y][0])*int(real_legit[y][1])
print(summ)
