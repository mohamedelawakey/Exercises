#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    long long arr[100005];

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    bool sorted = true;

    for (int i = 0; i < n - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            sorted = false;
            break;
        }
    }

    if (sorted) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }

    return 0;
}
