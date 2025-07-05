#include <iostream>
#include <algorithm>
#include <cctype>
using namespace std;
int main(){
    int n;
    cin >> n;

    string s;
    cin >> s;

    for(int i = 0; i < n / 2; i++){
        if(s[i] != s[n - 1 - i]){
            cout << "NO\n";
            return 0;
        }
    }
    cout << "YES\n";
    return 0;
}