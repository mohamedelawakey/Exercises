#include <iostream>
using namespace std;
int main() {
    int a, b;
    cin >> a >> b;

    bool found = false;

    for(int i = a; i <= b; i++){
        int temp = i;
        int is_luckey = true;

        while(temp > 0){
            int digit = temp % 10;

            if(digit != 4 && digit != 7){
                is_luckey = false;
                break;
            }
            temp /= 10;
        }

        if(is_luckey){
            cout << i << " ";
            found = true;
        }
    }
    
    if(!found){
        cout << -1;
    }

    cout << "\n";

    return 0;
}