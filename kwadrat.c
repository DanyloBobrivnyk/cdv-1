#include <math.h>
#include <stdio.h>
int main(){
	float a;
	float b;
	float c;
	printf("Podaj a \n");
	scanf("%f",&a);
	printf("Podaj b \n");
	scanf("%f",&b);
	printf("Podaj wyraz wolny \n");
	scanf("%f",&c);
	
	float delta = b*b-4*a*c;
	
	printf("Delta = %f \n",delta);
	if(delta<0){
		printf("Brak rozwiazan");
	}
	else if(delta==0){
		float x = -b/(2*a);
		printf("Miejsce zerowe : \n x = %f",x);
	}
	else{
		float pd = sqrt(delta);
		float x1 = (-b+pd)/(2*a);
		float x2 = (-b-pd)/(2*a);
		printf("Miejsca zerowe : \nx1 = %f \nx2 = %f",x1,x2);
	}
}
