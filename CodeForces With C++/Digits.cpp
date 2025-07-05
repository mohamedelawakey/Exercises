#include <iostream>
using namespace std;
int main() {
    int n ;
    cin >> n;

    for(int i = 0; i < n; i++){
        string x;
        cin >> x;

        for(int j = x.length() - 1; j >= 0 ; j--){
            cout << x[j];
            if(j != 0){
                cout << " ";
            }
        }
        cout << "\n";
    }
}