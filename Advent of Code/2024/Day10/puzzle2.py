f=open("input.txt",'r')
mapp=[]
while line:=f.readline():
	mapp.append(list(line.strip('\n')))
f.close()


def check_trail(coord,mapp):
	num=mapp[coord[1]][coord[0]]
	if num=="9":
		#if coord in coord_list:
		#	return 0
		#coord_list[coord]=1
		return 1
	summ=0
	did_something=0
	if coord[1]+1<len(mapp) and (mapp[coord[1]+1][coord[0]] == str(int(num)+1)):
		summ += check_trail((coord[0],coord[1]+1),mapp)
		did_something=1
	if coord[1]-1>=0 and (mapp[coord[1]-1][coord[0]] == str(int(num)+1)):
		summ+= check_trail((coord[0],coord[1]-1),mapp)
		did_something=1
	if coord[0]+1<len(mapp[0]) and (mapp[coord[1]][coord[0]+1] == str(int(num)+1)):
		summ+= check_trail((coord[0]+1,coord[1]),mapp)
		did_something=1
	if coord[0]-1>=0 and (mapp[coord[1]][coord[0]-1] == str(int(num)+1)):
		summ+= check_trail((coord[0]-1,coord[1]),mapp)
		did_something=1
	if did_something==0:
		return 0
	return summ
summ=0
for y in range(len(mapp)):
	for x in range(len(mapp)):
		if mapp[y][x]=="0":
			summ+=(check_trail((x,y),mapp))
print(summ)