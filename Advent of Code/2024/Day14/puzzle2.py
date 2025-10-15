import re
import numpy as np

f=open("input1.txt",'r')
a = f.readlines()
f.close()

size=(101,103)

class robot():
	def __init__(self,pos,vel,room):
		self.pos=pos
		self.vel=vel
		self.room=room
	def step(self):
		self.pos=((self.pos[0]+self.vel[0])%self.room[0],(self.vel[1]+self.pos[1])%self.room[1])

class bots():
	def __init__(self,size):
		self.bots = []
		self.size = size
	def add_bot(self,bot):
		self.bots.append(bot)
	def do_step(self,count=1):
		for i in range(count):
			for x in self.bots:
				x.step()
	def generate_table(self):
		self.table = np.zeros((self.size[1],self.size[0]))
		#indexed table[x][y], x=width y = height
		for i in self.bots:
			self.table[i.pos[1]][i.pos[0]]+=1
	def print_table(self):
		for line in self.table:
			for ch in line:
				print(int(ch),end='')
			print('')
	def get_quadrants(self):
		Q1=0
		Q2=0
		Q3=0
		Q4=0
		for x in range(0,(self.size[0]//2)):
			for y in range(0,(self.size[1]//2)):
				Q1+=self.table[y][x]
		for x in range(0,(self.size[0]//2)):
			for y in range((self.size[1]//2)+1,self.size[1]):
				Q2+=self.table[y][x]
		for x in range((self.size[0]//2)+1,self.size[0]):
			for y in range(0,(self.size[1]//2)):
				Q3+=self.table[y][x]
		for x in range((self.size[0]//2)+1,self.size[0]):
			for y in range((self.size[1]//2)+1,self.size[1]):
				Q4+=self.table[y][x]
		print(Q1,Q2,Q3,Q4)
		return Q1*Q2*Q3*Q4

def flood_find(table):
	count = 0
	for y in range(len(table)):
		for x in range(len(table[y])):
			if int(table[y][x]) > 0:
				count = max(count,flood_fill(table,x,y))
	return count

def flood_fill(table,x,y):
	if x < 0:
		return 0
	if y < 0:
		return 0
	if x >= len(table[0]):
		return 0
	if y >= len(table):
		return 0
	if int(table[y][x]) <= 0:
		return 0
	table[y][x]=0
	count = 0
	count += flood_fill(table,x,y+1)
	count += flood_fill(table,x,y-1)
	count += flood_fill(table,x+1,y)
	count += flood_fill(table,x-1,y)
	return 1+count

sim = bots(size)
for i in a:
	match = re.search(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)",i)
	sim.add_bot(robot((int(match.group(1)),int(match.group(2))),(int(match.group(3)),int(match.group(4))),size))
sim.generate_table()
step_counter=0
while True:
	temp=flood_find(sim.table)
	if temp > 20:
		break

	sim.do_step(1)
	step_counter+=1
	sim.generate_table()
sim.generate_table()
sim.print_table()
print(temp)
print(step_counter)
