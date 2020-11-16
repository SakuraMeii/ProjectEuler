#include <iostream>
using namespace std;

const int  maxNum = 2000000;

int main(){
  int primeList[1000000];
  primeList[0] = 2;
  int index = 1;
  for(int i=3;i<maxNum;i+=2){
    for(int j=0;j<index;j++){
      //cout << i << "," << j << "," << primeList[j] << endl;
      if(i % primeList[j] == 0){
        if(j == index-1){
          primeList[index] = i;
          index++;
        }
        break;
      }else{
        if(j == index-1){
          primeList[index] = i;
          index++;
          break;
        }
      }
    }
  }
  long int sum = 0;
  for(int i=0;i<index;i++){
    //cout << primeList[i] << endl;
    sum+=primeList[i];
  }
  cout << sum << endl;
}
