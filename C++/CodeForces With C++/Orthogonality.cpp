#include <iostream>
using namespace std;
int main(){
    int n ;
    cin >> n;

    int X[100001], B[100001];

    for(int i = 0; i < n; i++){
        cin >> X[i];
    }

    for(int i = 0; i < n; i++){
        cin >> B[i];
    }

    long long dot_product = 0;

    for(int i = 0; i < n; i++){
        dot_product += (long long) X[i] * B[i];
    }

    if(dot_product == 0){
        cout << "Yes\n";
    }
    else{
        cout << "No\n";
    }
}