#include <iostream>
using namespace std;

int Fibonacci(int n);
int main(){
	int sum{0};
	int n{1};
        while(true){
		int a = Fibonacci(n);
		if(a >= 4000000){
			break;
		}
		else{
			if(a % 2 == 0)
				sum += a;
		}
		n++;
	}
	cout << sum << endl;
	return 0;
}

int Fibonacci(int n){
	if(n == 1)
		return 1;
	if(n == 2)
		return 2;
	return Fibonacci(n-1)+Fibonacci(n-2);
}

