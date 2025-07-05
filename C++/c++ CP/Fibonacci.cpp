#include <iostream>
#include <algorithm>
#include <cctype>
using namespace std;
int main(){
    int n;
    cin >> n;

    long long fib[51];

    fib[1] = 0;
    fib[2] = 1;

    for(int i = 3; i <= n; i++){
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    for(int i = 1; i <= n; i++){
        cout << fib[i] << " ";
    }

    cout << "\n";
}