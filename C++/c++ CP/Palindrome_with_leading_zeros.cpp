#include <iostream>
using namespace std;

int main() {
    string s;
    cin >> s;

    while (!s.empty() && s.back() == '0') {
        s.pop_back();  
    }

    string reversed = s;
    
    for (int i = 0, j = reversed.size() - 1; i < j; i++, j--) {
        swap(reversed[i], reversed[j]);
    }

    if (s == reversed) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}
