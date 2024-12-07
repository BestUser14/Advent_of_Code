f=open("input.txt",'r')
total=[]
ins=[]
while(line:=f.readline()):
    temp=line.split(': ')
    total.append(temp[0])
    ins.append(temp[1].strip('\n').split(' '))
f.close()

def could_be(total,inputs):
    ret = 0
    operators=ops(len(inputs)-1)
    for op_list in operators:
        summ=int(inputs[0])
        for operate in range(len(op_list)):
            if op_list[operate] == '+':
                summ+=int(inputs[operate+1])
            if op_list[operate] == '*':
                summ*=int(inputs[operate+1])
        if summ==int(total):
            return int(total)
    return 0

def ops(length):
    if length==1:
        return ['*','+']
    out=[]
    nex = ops(length-1)
    for i in range(len(nex)):
        out.append(nex[i]+'*')
        out.append(nex[i]+'+')
    return out
summ=0
for i in range(len(total)):
    summ+=could_be(total[i],ins[i])
print(summ)
