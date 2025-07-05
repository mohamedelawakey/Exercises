#include <iostream>
#include <algorithm>
#include <cctype>
using namespace std;
int main(){
    int n;
    cin >> n;

    string s;

    for(int i = 0; i < n; i++){
        cin >> s;

        int sum1 = (s[0] - '0') + (s[1] - '0') + (s[2] - '0');
        int sum2 = (s[3] - '0') + (s[4] - '0') + (s[5] - '0');

        if(sum1 == sum2){
            cout << "YES\n";
        }
        else{
            cout << "NO\n";
        }
    }
}