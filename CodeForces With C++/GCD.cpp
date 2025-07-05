// GCD

#include <iostream>
using namespace std;

int main(){
    int num1, num2, GCD;

    cin >> num1 >> num2;

    for(int i = 1; i <= min(num1, num2); i++) {
        if(num1 % i == 0 and num2 % i == 0){
            GCD = i;
        }
    }

    cout << GCD << "\n";
}