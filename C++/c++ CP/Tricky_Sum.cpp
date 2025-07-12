#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        long long n;
        cin >> n;

        long long total_sum = n * (n + 1) / 2;

        long long power = 1;
        long long powers_sum = 0;

        while (power <= n) {
            powers_sum += power;
            power *= 2;
        }
        
        cout << total_sum - 2 * powers_sum << "\n";
    }

    return 0;
}
