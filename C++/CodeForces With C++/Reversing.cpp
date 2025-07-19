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

    for(int i = n - 1; i >= 0; i--){
        cout << L[i] << " ";
    }
}