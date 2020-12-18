#include <iostream>
using namespace std;

bool evenDivide(int n, int upperLimit);
int main(){
  int n = 21;
  while(true){
    if(evenDivide(n,20) == false){
      n++;
    }else{
      break;
    }
  }
  cout << n << endl;
}
bool evenDivide(int n, int upperLimit){
  for(int i=1;i<=upperLimit;i++){
    if(n % i != 0){
      return false;
    }
  }
  return true;
}
