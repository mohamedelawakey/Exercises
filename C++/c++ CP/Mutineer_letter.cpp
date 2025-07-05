#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    string s;
    cin >> s;

    for (int i = 0; i < n; i++) {
        if (s[i] >= 'A' && s[i] <= 'Z') {
            cout << s[i] << " " << (i + 1) << "\n";
            break;
        }
    }

    return 0;
}
