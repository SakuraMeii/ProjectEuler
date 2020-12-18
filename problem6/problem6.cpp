#include <iostream>
using namespace std;

int sumSquareDiff(int n);
int main(){
  cout << sumSquareDiff(100) << endl;
}

int sumSquareDiff(int n){
  int sum = 0;
  int square = 0;
  for(int i=1;i<=n;i++){
    sum += i*i;
    square += i;
  }
  square *= square;
  return square-sum;
}
