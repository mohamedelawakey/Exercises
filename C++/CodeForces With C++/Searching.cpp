#include <iostream>
#include <vector>
using namespace std;
int main(){
    int n;
    cin >> n;

    vector<int> L(n);
    for(int i = 0; i < n; i++){
        cin >> L[i];
    }

    int target;
    cin >> target;

    for(int i = 0; i < n; i++){
        if(L[i] == target){
            cout << i << "\n";
            return 0;
        }
    }

    cout << -1 << "\n";
    return 0;
}