#include <iostream>
using namespace std;

int ABC(int n){
    if(n <= 0){
        return 0;
    }

    return n + ABC(n - 1);
}

int main(){
    int n;
    cin >> n;

    cout << ABC(n) << endl;
}