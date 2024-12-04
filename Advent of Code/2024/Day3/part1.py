import re
f=open("input.txt",'r')
inp=""
while(temp := f.readline()):
    inp=inp+temp
f.close()

legit = re.findall(r"mul\([0-9]+,[0-9]+\)",inp)

real_legit=[]
for x in range(len(legit)):
    real_legit.append(legit[x][4:-1].split(','))

summ=0
for y in range(len(real_legit)):
    summ+= int(real_legit[y][0])*int(real_legit[y][1])
print(summ)
