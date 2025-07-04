#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    string s, t;
    cin >> s >> t;

    for (int i = 0; i <= n - 3; i++) {
        if (s[i] == t[0] && s[i + 1] == t[1] && s[i + 2] == t[2]) {
            cout << "YES\n";
            return 0;
        }
    }

    cout << "NO\n";
    return 0;
}
