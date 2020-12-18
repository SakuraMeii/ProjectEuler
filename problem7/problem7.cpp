#include <iostream>
using namespace std;
const int question = 10001;
int main(){
  int prime[question];
  prime[0] = 2;
  int n = 3;
  int amount = 1;
  bool isPrime = true;
  while(amount < question){
    isPrime = true;
    for(int i=2;i<n;i++){
      if(n % i == 0){
        //cout << n << " " << i << endl;
        isPrime = false;
        n++;
        break;
      }
    }
    if(isPrime == true){
      prime[amount++] = n++;
      //cout << amount+1 << " " << n << endl;
    }
  }
  cout << prime[question-1] << endl;
}
