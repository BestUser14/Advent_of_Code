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
	neg_counter=-1
	neg_temp=-1
	counter_temp=0
	counter=0
	while length+neg_counter>=0:
		if drive[neg_counter]=='.':
			while neg_counter+length>=0 and drive[neg_counter]=='.':
				neg_counter-=1
		neg_temp=neg_counter
		while neg_temp+length>=0 and drive[neg_temp]==drive[neg_counter]:
			neg_temp-=1
		counter=0
		while counter <= (neg_temp+length):
			while counter<len(drive) and drive[counter]!='.':
				counter+=1
			temp_counter=counter
			while temp_counter < len(drive) and drive[temp_counter]=='.':
				temp_counter+=1
			if temp_counter>length+neg_counter:
				break
			if temp_counter-counter>=-1*(neg_temp-neg_counter):
				for x in range(-1*(neg_temp-neg_counter)):
					drive[counter+x]=drive[neg_counter-x]
					drive[neg_counter-x]='.'
				break
			counter=temp_counter+1
		neg_counter=neg_temp
	return drive
def checksum(drive):
	counter=0
	output=0
	for i in range(len(drive)):
		if drive[i] != '.':
			output+=i*int(drive[i])
	return output
print(checksum(fix_drive(parse(drive))))