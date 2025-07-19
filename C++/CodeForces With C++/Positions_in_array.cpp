#include <iostream>
#include <vector>
using namespace std;
int main(){
    int n;
    cin >> n;

    vector<int> L(n);

    for(int i = 0; i <n; i++){
        cin >> L[i];
    }

    for(int i = 0; i <n; i++){
        if(L[i] <= 10){
            cout << "A[" << i << "] = " <<  L[i] <<"\n";
        }
    }
}