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

    int min_value = L[0];
    int min_index = 0;

    for(int i = 1; i < n; i++){
        if(L[i] < min_value){
            min_value = L[i];
            min_index = i;
        }
    }
    
    cout << min_value << " " << min_index + 1 << "\n";
}