#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        long long a[150005];
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        long long min_price = a[n - 1];
        int bad_days = 0;

        for (int i = n - 2; i >= 0; i--) {
            if (a[i] > min_price) {
                bad_days++;
            } else {
                min_price = a[i];
            }
        }

        cout << bad_days << "\n";
    }

    return 0;
}
