#include <iostream>
using namespace std;
int main(){
    int num1, k;

    cin >> num1 >> k;

    for(int i = 0; i < k; i++){
        if(num1 % 10 == 0){
            num1 /= 10;
        }
        else{
            num1 -= 1;
        }
    }

    cout << num1 << "\n";
}