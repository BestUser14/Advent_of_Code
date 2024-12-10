f=open("input.txt",'r')
inputs=[]
while line:=f.readline():
	inputs.append(list(line.strip('\n')))
f.close()
antinodes={}

def find_anti(first,second,array):
	delta_x=second[0]-first[0]
	delta_y=second[1]-first[1]
	nodes=0
	pos1=(first[0]-delta_x,first[1] - delta_y)
	pos2=(second[0]+delta_x,second[1]+delta_y)
	if (first[0]-delta_x >=0) and (first[0]-delta_x <len(array[0])) and (first[1] - delta_y >= 0) and (first[1] - delta_y < len(array)):
		if pos1 not in antinodes:
			nodes+=1
			antinodes[pos1]=1
	if ((second[0]+delta_x) < len(array[0])) and ((second[0]+delta_x) >=0) and ((second[1]+delta_y) >-0) and ((second[1]+delta_y) < len(array)):
		if pos2 not in antinodes:
			nodes+=1
			antinodes[pos2]=2
	return nodes

def find_pairs(node,array):
	signal = array[node[1]][node[0]]
	anti_pairs=0
	for x in range((node[0]+1),len(array[0])):
		if array[node[1]][x]==signal:
			anti_pairs+=find_anti(node,(x,node[1]))
	for y in range(node[1]+1,len(array)):
		for x in range(len(array[0])):
			if array[y][x]==signal:
				anti_pairs+=find_anti(node,(x,y),array)
	return anti_pairs

out=0
for y in range(len(inputs)):
	for x in range(len(inputs[y])):
		if inputs[y][x] != '.' and inputs[y][x]!='#':
			out+=find_pairs((x,y),inputs)
print(out)