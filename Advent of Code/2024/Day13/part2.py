import re

def get_x(A,B,G):
	return (int(B[0])*int(G[1])-int(B[1])*int(G[0]))//(int(B[0])*int(A[1])-int(B[1])*int(A[0]))
def get_y(A,B,G):
	return (int(A[0])*int(G[1])-int(A[1])*int(G[0]))//(int(A[0])*int(B[1])-int(A[1])*int(B[0]))
f=open("input1.txt",'r')
a=f.readlines()
f.close()

cost = 0
count = 0

for i in range((len(a)//4)+1):
	match = re.search(r"Button A: X\+(\d+), Y\+(\d+)",a[i*4].strip())
	A=match.groups()
	match = re.search(r"Button B: X\+(\d+), Y\+(\d+)",a[i*4+1].strip())
	B=match.groups()
	match = re.search(r"Prize: X=(\d+), Y=(\d+)",a[i*4+2].strip())
	G=match.groups()

	G = (str(int(G[0])+10000000000000),(str(int(G[1])+10000000000000)))
	X=get_x(A,B,G)
	Y=get_y(A,B,G)
	if int(A[0])*int(X)+int(B[0])*int(Y)==int(G[0]) and int(A[1])*int(X)+int(B[1])*int(Y)==int(G[1]) and int(X)>0 and int(Y)>0:
		cost+=3*int(X)+int(Y)
		count+=1
print(count,cost)
