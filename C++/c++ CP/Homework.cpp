#include <iostream>
#include <algorithm>
#include <cctype>
using namespace std;
int main(){
    int n; 
    cin >> n;

    string s;
    cin >> s;

    int counter = 0;

    for(int i = 0; i < n; i++){
        char c = s[i];

        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
            counter++;
        }
    }

    cout << counter << "\n";
}