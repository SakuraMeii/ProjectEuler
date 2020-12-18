#include <iostream>
using namespace std;

int maxPrime(long int num);
int nextPrime(int prime);
int main(){
	long int a = 600851475143;
        cout << maxPrime(a) << endl;
	return 0;
}

int maxPrime(long int num){
	int prime = 2;
	while(true){
		if(num == prime)
			return prime;
		if(num % prime == 0){
			num /= prime;
		}
		else{
                        prime++;
		}
	}
}
int nextPrime(int prime){
	return 0;
}
