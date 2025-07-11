#include <iostream>
using namespace std;

int main() {
    int n, top;
    cin >> n >> top;

    int bottom = 7 - top;

    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;

        if (a == top || a == bottom || b == top || b == bottom) {
            cout << "NO\n";
            return 0;
        }
    }

    cout << "YES\n";
    return 0;
}