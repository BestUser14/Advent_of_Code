f=open("input.txt",'r')
drive=f.readline().strip('\n')
f.close()


def parse(drive):
	new_drive=[0]*int(drive[0])
	counter=1
	for i in range(1,len(drive),2):
		new_drive.extend(['.']*int(drive[i]))
		new_drive.extend([counter]*int(drive[i+1]))
		counter+=1
	return new_drive
def fix_drive(drive):
	length=len(drive)
	negative_counter=-1
	for i in range(len(drive)):
		if drive[i]=='.':
			while(negative_counter>=-1*length and drive[negative_counter]=='.'):
				negative_counter-=1
			if negative_counter + length<= i:
				break
			drive[i]=drive[negative_counter]
			drive[negative_counter]='.'
	return drive
def checksum(drive):
	counter=0
	length=len(drive)
	output=0
	while(counter<length and drive[counter]!='.'):
		output+=counter*drive[counter]
		counter+=1
	return output
print(checksum(fix_drive(parse(drive))))