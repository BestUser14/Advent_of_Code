inn=[0, 5601550, 3914, 852, 50706, 68, 6, 645371]

def rule(item):
	if item==0:
		return [1]
	if len(str(item))%2==0 and len(str(item))!=0:
		return [int(str(item)[:len(str(item))//2]),int(str(item)[len(str(item))//2:])]
	return [item*2024]
def rule_list(lis):
	temp=[]
	for i in range(len(lis)):
		temp.extend(rule(lis[i]))
	return temp
for i in range(40):
	inn=rule_list(inn)
#print(len(inn))
