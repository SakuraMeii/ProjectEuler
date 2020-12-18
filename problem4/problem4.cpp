#include <iostream>
#include <climits>
using namespace std;

bool palindrome(int a);
int main(){
  int minPalindrome = INT_MIN;
  for(int i=100;i<1000;i++){
    for(int j=100;j<1000;j++){
      if(palindrome(i*j) && i*j > minPalindrome){
        minPalindrome = i*j;
      }
    }
  }
  cout << minPalindrome << endl;
}

bool palindrome(int a){
  int tmp = a;
  int reverseNum = 0;
  while(tmp != 0){
    reverseNum = reverseNum*10+tmp%10;
    tmp /= 10;
  }
  return reverseNum == a;
}
