f=open("input.txt",'r')
table=[]
while(line:=f.readline()):
    table.append(list(line))
f.close()

def find(array,word,x,y):
    direction=[[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,-1],[-1,1],[1,-1]]
    ret=0
    temp_counter=0
    for i in range(len(direction)):
        temp_x=0
        temp_y=0
        for b in range(len(word)):
            if x+temp_x <0 or x+temp_x >= len(array[0]):
                break
            if y+temp_y<0 or y+temp_y >= len(array):
                break
            if array[y+temp_y][x+temp_x]!=word[b]:
                break
            temp_counter+=1
            temp_x+=direction[i][0]
            temp_y+=direction[i][1]
        if temp_counter==len(word):
            ret+=1
        temp_counter=0
    return ret
counter=0
for x in range(len(table)):
    for y in range(len(table)):
        counter+=find(table,"XMAS",x,y)
print(counter)
