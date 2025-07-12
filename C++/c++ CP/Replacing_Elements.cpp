#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, d;
        cin >> n >> d;

        int a[100];
        int min1 = 101, min2 = 101;
        bool allOk = true;

        for (int i = 0; i < n; i++) {
            cin >> a[i];
            if (a[i] > d) allOk = false;

            if (a[i] < min1) {
                min2 = min1;
                min1 = a[i];
            } else if (a[i] < min2) {
                min2 = a[i];
            }
        }

        if (allOk || min1 + min2 <= d)
            cout << "YES\n";
        else
            cout << "NO\n";
    }

    return 0;
}