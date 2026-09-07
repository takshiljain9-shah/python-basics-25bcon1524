#include <stdio.h> 
int main(){
int num = 5;
int fact = 1; 
for (int i = 0; i <= num; i++){
fact *= i;
}
printf("Factorial of the %d is : %llu\n", num, fact);
return 0;
}
