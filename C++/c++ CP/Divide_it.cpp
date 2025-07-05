#include <iostream>

using namespace std;

int main() {
    int q;
    cin >> q;
    while (q--) {
        long long n;
        cin >> n;
        long long steps = 0;
        while (n != 1) {
            if (n % 2 == 0) {
                n /= 2;
                steps++;
            } else if (n % 3 == 0) {
                n = (2 * n) / 3;
                steps++;
            } else if (n % 5 == 0) {
                n = (4 * n) / 5;
                steps++;
            } else {
                steps = -1;
                break;
            }
        }
        cout << steps << endl;
    }
    return 0;
}