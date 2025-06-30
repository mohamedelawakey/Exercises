#include <iostream>
using namespace std;
int main(){
    int n, k;
    cin >> n >> k;

    int coin = 500;

    if(n * coin >= k){
        cout << "Yes\n";
    }
    else{
        cout << "No\n";
    }
}