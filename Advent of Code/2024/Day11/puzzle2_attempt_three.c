#include<stdio.h>
#include"stupid2.h"


int main(){
	int inn[]={0, 5601550, 3914, 852, 50706, 68, 6, 645371};
	unsigned long long memoization[MAX_ARRAY][BLINK];
	for(int x=0;x<BLINK;x++){
		for (int y=0;y<MAX_ARRAY;y++){
			memoization[y][x]=0;
		}
	}
	unsigned long long out=0;
	for(int i=0;i<8;i++){
		out+=recursive_rule(inn[i],BLINK,memoization);
	}
	printf("%llu\n",out);
	return 1;
}

unsigned long long recursive_rule(unsigned long long item, unsigned long long again, unsigned long long memoize[MAX_ARRAY][BLINK]){
	if (item<MAX_ARRAY){
		unsigned long long super_output=memoize[item][again];
		if(again==0){
			return 1;
		}
		else if (super_output==0){
			if(item==0){
				memoize[item][again] = recursive_rule(1,again-1,memoize);
				return memoize[item][again];
			}
			if(even_digit(item)){
				memoize[item][again]=do_op_three(item,again-1,memoize);
				return memoize[item][again];
			}
			memoize[item][again]= recursive_rule(item*2024,again-1,memoize);
			return memoize[item][again];
		}
		else {
			return memoize[item][again];
		}
	}
	if(again==0){
		return 1;
	}
	if(item==0){
		return recursive_rule(1,again-1,memoize);
	}
	if(even_digit(item)){
		return do_op_three(item,again-1,memoize);
	}
	return recursive_rule(item*2024,again-1,memoize);
}	

unsigned long long even_digit(unsigned long long item){
	if(item<10u){
		return 0;
	}
	else if(item<100u){
		return 1;
	}
	else if(item<1000u){
		return 0;
	}
	else if(item<10000u){
		return 1;
	}
	else if(item<100000u){
		return 0;
	}
	else if(item<1000000u){
		return 1;
	}
	else if(item<10000000u){
		return 0;
	}
	else if(item<100000000u){
		return 1;
	}
	else if(item<1000000000u){
		return 0;
	}
	else if(item<10000000000u){
		return 1;
	}
	else if(item<100000000000u){
		return 0;
	}
	else if(item<1000000000000u){
		return 1;
	}
	else if(item<10000000000000u){
		return 0;
	}
	else if(item<100000000000000u){
		return 1;
	}
	else if(item<1000000000000000u){
		return 0;
	}
	else if(item<10000000000000000u){
		return 1;
	}
	else if(item<100000000000000000u){
		return 0;
	}
	else if(item<1000000000000000000u){
		return 1;
	}
	else if(item<10000000000000000000u){
		return 0;
	}
	else{
		return 1;
	}
}

unsigned long long do_op_three(unsigned long long item, unsigned long long again, unsigned long long memoize[MAX_ARRAY][BLINK]){
	if(item<100u){
		return recursive_rule((item)/10,again,memoize)+recursive_rule(item%10,again,memoize);
	}
	else if(item<10000u){
		return recursive_rule((item)/100,again,memoize)+recursive_rule(item%100,again,memoize);
	}
	else if(item<1000000u){
		return recursive_rule((item)/1000,again,memoize)+recursive_rule(item%1000,again,memoize);
	}
	else if(item<100000000u){
		return recursive_rule((item)/10000,again,memoize)+recursive_rule(item%10000,again,memoize);
	}
	else if(item<10000000000u){
		return recursive_rule((item)/100000,again,memoize)+recursive_rule(item%100000,again,memoize);
	}
	else if(item<1000000000000u){
		return recursive_rule((item)/1000000,again,memoize)+recursive_rule(item%1000000,again,memoize);
	}
	else if(item<100000000000000u){
		return recursive_rule((item)/10000000,again,memoize)+recursive_rule(item%10000000,again,memoize);
	}
	else if(item<10000000000000000u){
		return recursive_rule((item)/100000000,again,memoize)+recursive_rule(item%100000000,again,memoize);
	}
	else if(item<1000000000000000000u){
		return recursive_rule((item)/1000000000,again,memoize)+recursive_rule(item%1000000000,again,memoize);
	}
	else{
		return recursive_rule((item)/10000000000,again,memoize)+recursive_rule(item%10000000000,again,memoize);
	}
}
