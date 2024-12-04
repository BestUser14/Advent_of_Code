f=open("input.txt",'r')
tests=[]
while(line:=f.readline()):
    temp=(line.split(' '))
    for i in range(len(temp)):
        temp[i]=int(temp[i])
    tests.append(temp)
f.close()
      
def test(array):
    greater=0
    lesser=0
    for i in range(len(array)-1):
        if array[i]>array[i+1]:
            greater+=1
        if array[i]<array[i+1]:
            lesser+=1
    if greater!=len(array)-1 and lesser!=len(array)-1:
        return 0
    for i in range(len(array)-1):
        if abs(array[i]-array[i+1])>3 or abs(array[i]-array[i+1])<=0:
            return 0
    return 1

def double_test(array):
    safe=0
    temp=[]
    for i in range(len(array)):
        temp=array.copy()
        temp.pop(i)
        safe+=test(temp)
    if safe>0:
        return 1
    return 0

safeno=0

for i in range(len(tests)):
    safeno+=double_test(tests[i])
print(safeno)
