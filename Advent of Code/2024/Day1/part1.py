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

for i in range(len(lis1)):
    ans+=abs(int(lis1[i])-int(lis2[i]))
print(ans)
