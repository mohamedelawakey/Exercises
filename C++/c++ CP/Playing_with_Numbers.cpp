#include <iostream>
#include <algorithm>
#include <cctype>
using namespace std;
int main(){
    string n; 
    cin >> n;

    reverse(n.begin(),n.end());

    int i = 0;

    while(n[i] == '0'){
        i++;
    }

    cout << n.substr(i) << "\n";
}