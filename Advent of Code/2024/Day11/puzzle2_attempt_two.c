#include<stdio.h>
#include"stupid.h"

int main(){
	int inn[]={0, 5601550, 3914, 852, 50706, 68, 6, 645371};
	long long int out=0;
	for(int i=0;i<8;i++){
		out+=recursive_rule(inn[i],40);
	}
	printf("%llu\n",out);
	return 1;
}

unsigned long long recursive_rule(unsigned long long item, int again){
	if(again==0){
		return 1;
	}
	if(item==0){
		return recursive_rule(1,again-1);
	}
	if(even_digit(item)){
		return do_op_three(item,again-1);
	}
	return recursive_rule(item*2024,again-1);
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

unsigned long long do_op_three(unsigned long long item, int again){
	if(item<100u){
		return recursive_rule((item)/10,again)+recursive_rule(item%10,again);
	}
	else if(item<10000u){
		return recursive_rule((item)/100,again)+recursive_rule(item%100,again);
	}
	else if(item<1000000u){
		return recursive_rule((item)/1000,again)+recursive_rule(item%1000,again);
	}
	else if(item<100000000u){
		return recursive_rule((item)/10000,again)+recursive_rule(item%10000,again);
	}
	else if(item<10000000000u){
		return recursive_rule((item)/100000,again)+recursive_rule(item%100000,again);
	}
	else if(item<1000000000000u){
		return recursive_rule((item)/1000000,again)+recursive_rule(item%1000000,again);
	}
	else if(item<100000000000000u){
		return recursive_rule((item)/10000000,again)+recursive_rule(item%10000000,again);
	}
	else if(item<10000000000000000u){
		return recursive_rule((item)/100000000,again)+recursive_rule(item%100000000,again);
	}
	else if(item<1000000000000000000u){
		return recursive_rule((item)/1000000000,again)+recursive_rule(item%1000000000,again);
	}
	else{
		return recursive_rule((item)/10000000000,again)+recursive_rule(item%10000000000,again);
	}
}
