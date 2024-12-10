from copy import deepcopy
f=open("input.txt",'r')
mapp=[]
counter=0
while(line:=f.readline()):
    mapp.append(list(line))
f.close()

pos=(0,0)
for y in range(len(mapp)):
    for x in range(len(mapp[y])):
        counter+=1
        if mapp[y][x]=='^':
            pos=(x,y)

def move(x,y,mapp,direction):
    x+=direction[0]
    y+=direction[1]
    if x<0 or y<0 or x>=len(mapp[0]) or y>=len(mapp):
        return -1
    if mapp[y][x]=='#':
        x-=direction[0]
        y-=direction[1]
        if direction == (1,0):
            direction = (0,1)
        elif direction == (-1,0):
            direction = (0,-1)
        elif direction == (0,1):
            direction = (-1,0)
        else:
            direction =(1,0)
    return [x,y,direction]
def check(pos,mapp,counter):
    direction=(0,-1)
    has_been={((pos[0],pos[1],direction[0],direction[1])):1}
    while(counter>0):
        counter-=1
        out=move(pos[0],pos[1],mapp,direction)
        if out==-1:
            return 0
        pos=[out[0],out[1]]
        direction=out[2]
        if has_been.get(((pos[0],pos[1],direction[0], direction[1]))) != None:
            return 1
        has_been[(pos[0],pos[1],direction[0],direction[1])]=1
    return 0
def get_path(pos,mapp,counter):
    direction=(0,-1)
    path=[pos]
    while((out:=move(pos[0],pos[1],mapp,direction))!=-1):
        pos=[out[0],out[1]]
        direction=out[2]
        if pos not in path:
            path.append(pos)
    return path
path=get_path(pos,mapp,counter)
summ=0
for x in path:
    if mapp[x[1]][x[0]] != '#' and mapp[x[1]][x[0]] != '^':
        temp_hold = mapp[x[1]][x[0]]
        mapp[x[1]][x[0]]='#'
        summ+=check(pos,mapp,counter)
        mapp[x[1]][x[0]]=temp_hold
print(summ)
