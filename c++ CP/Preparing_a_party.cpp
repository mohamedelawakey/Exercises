#include <iostream>
#include <cmath>
#include <climits> 

using namespace std;

int main() {
    int n;
    cin >> n;

    long long a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    long long max_diff = 0;
    long long min_diff = LLONG_MAX;

    for (int i = 0; i < n - 1; i++) {
        long long diff = abs(a[i] - a[i + 1]);
        max_diff = max(max_diff, diff);
        min_diff = min(min_diff, diff);
    }

    cout << max_diff << " " << min_diff << endl;
    return 0;
}
