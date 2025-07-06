#include <iostream>
using namespace std;
int main() {
    int num1, num2;

    while(true){
        cin >> num1 >> num2;
        if(num1 <= 0 || num2 <= 0){
            break;
        }

        int start = min(num1, num2);
        int end = max(num1, num2);
        int sum = 0;

        for(int i = start; i <= end; i++){
            cout << i << " ";
            sum +=i;
        }
        cout << "sum =" << sum << '\n';
    }
}