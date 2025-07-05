#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    long long a[200005];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    long long x;
    cin >> x;

    for (int i = 0; i < n; i++) {
        if (a[i] == x) {
            cout << i << endl;
            return 0;
        }
    }

    cout << -1 << endl;
    return 0;
}
