#include <iostream>
using namespace std;
int main(){
    int a, b, c;
    int num;
    cin >> num;

    for(int i = 0; i < num; i++){
        cin >> a >> b >> c;

        if (a + b >= 10 || a + c >= 10 || b + c >= 10){
            cout << "YES\n";
        }
        else{
            cout << "NO\n";
        }
    }
}