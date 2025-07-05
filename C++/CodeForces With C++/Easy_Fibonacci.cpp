#include <iostream>
using namespace std;

int main(){
    int x;
    cin >> x;

    long long fib[46];

    fib[1] = 0;
    fib[2] = 1;
    
    for(int i = 3; i <= x; i++){
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    for(int i = 1; i <= x; i++){
        cout << fib[i] << " ";
    }

    cout << "\n";
}