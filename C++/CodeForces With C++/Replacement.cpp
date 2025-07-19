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
        if(L[i] > 0){
            L[i] = 1;
        }
        else if(L[i] < 0){
            L[i] = 2;
        }
    }

    for(int i = 0; i <n; i++){
        cout << L[i] << " ";
    }
}