f=open("input.txt",'r')
table=[]
while(line:=f.readline()):
    table.append(list(line))
f.close()

def find(array,x,y):
    ret=0
    if array[y][x]=="A":
        if (array[y+1][x+1]=="M" and array[y-1][x-1]=="S"):
            ret+=1
        if (array[y-1][x+1]=="M" and array[y+1][x-1]=="S"):
            ret+=1
        if (array[y-1][x-1]=="M" and array[y+1][x+1]=="S"):
            ret+=1
        if (array[y+1][x-1]=="M" and array[y-1][x+1]=="S"):
            ret+=1
    if ret>=2:
        return 1
    return 0
counter=0
for x in range(len(table)-2):
    for y in range(len(table)-2):
        counter+=find(table,x+1,y+1)
print(counter)
