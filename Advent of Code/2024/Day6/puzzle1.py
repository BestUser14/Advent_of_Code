import copy
f=open("input.txt",'r')
mapp=[]
while(line:=f.readline()):
    mapp.append(list(line))
f.close()

map_copy = copy.deepcopy(mapp)
pos=[0,0]
for y in range(len(mapp)):
    for x in range(len(mapp[y])):
        map_copy[y][x]=0
        if mapp[y][x]=='^':
            map_copy[y][x]=1
            pos=[x,y]

def move(x,y,mapp,direction):
    x+=direction[0]
    y+=direction[1]
    if x<0 or y<0 or x>=len(mapp[0]) or y>=len(mapp):
        return -1
    if mapp[y][x]=='#':
        x-=direction[0]
        y-=direction[1]
        if direction == [1,0]:
            direction = [0,1]
        elif direction == [-1,0]:
            direction = [0,-1]
        elif direction == [0,1]:
            direction = [-1,0]
        else:
            direction =[1,0]
    return [x,y,direction]
direction=[0,-1]
while((out:=move(pos[0],pos[1],mapp,direction))!=-1):
    pos=(out[0],out[1])
    direction=out[2]
    map_copy[pos[1]][pos[0]]=1
summ=0

for i in range(len(map_copy)):
    summ+=sum(map_copy[i])
print(summ)
