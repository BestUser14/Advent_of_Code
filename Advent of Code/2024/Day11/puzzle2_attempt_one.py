inn=[0, 5601550, 3914, 852, 50706, 68, 6, 645371]

def recursive_rule(item,again):
	if again==0:
		return 1
	if item == 0:
		return recursive_rule(1,again-1)
	elif len(str(item))%2==0:
		out=recursive_rule(int(str(item)[:len(str(item))//2]),again-1)
		return out+ recursive_rule(int(str(item)[len(str(item))//2:]),again-1)
	return recursive_rule(item*2024,again-1)
out=0
for i in range(len(inn)):
	out+=recursive_rule(inn[i],40)
#print(out)
