#include <iostream>
#include <cmath> 
using namespace std;
int main(){
    int n;
    int sum = 0;
    cin >> n;

    for(int i = n; i > 0; i--){
        sum += i;
    }

    cout << sum << "\n";
}