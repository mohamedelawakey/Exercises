#include <iostream>
using namespace std;
int main(){
    string n ;
    cin >> n;

    string new_n = "";

    for(int i = 0; i < n.length(); i++){
        if(n[i] == '.'){
            break;
        }
        new_n += n[i];
    }
    cout << new_n << "\n";
}