#include <iostream>
using namespace std;

int main(){
    int num;
    cin >> num;

    for(int i = 1; i <= num; i++){
        bool luckey = true;
        int x = i;

        while(x > 0){
            int digit = x % 10;
            if(digit != 4 && digit != 7){
                luckey = false;
                break;
            }
            x /= 10;
        }

        if(luckey && num % i == 0){
            cout << "YES\n";
            return 0;
        }
    }
    cout << "NO\n";
}
