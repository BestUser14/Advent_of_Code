lis1 = []
lis2 = []

f=open("input1.txt",'r')
counter=0
while(line:=f.readline()):
    lis1.append(line.split('   ')[0])
    lis2.append(line.split('   ')[1].strip('\n'))
f.close()
lis1.sort()
lis2.sort()

ans=0
counter={}

for x in range(len(lis2)):
    if lis2[x] in counter.keys():
        counter[lis2[x]]+=1
    else:
        counter[lis2[x]]=1
for i in range(len(lis1)):
    if lis1[i] in counter.keys():
        ans+=int(lis1[i])*counter[lis1[i]]
print(ans)
