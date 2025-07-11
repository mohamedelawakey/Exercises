#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    string s;
    cin >> s;

    string numbers = "";
    for (int i = 0; i < s.size(); i++) {
        if (s[i] != '+') {
            numbers += s[i];
        }
    }

    sort(numbers.begin(), numbers.end());

    for (int i = 0; i < numbers.size(); i++) {
        if (i > 0){
            cout << '+';
        } 
        cout << numbers[i];
    }

    cout << "\n";
    return 0;
}
