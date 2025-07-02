#include <iostream>
#include <string>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    int counter = 0;

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;

        bool digits[10] = {false};

        for (char c : s) {
            digits[c - '0'] = true;
        }

        bool good = true;
        for (int d = 0; d <= k; d++) {
            if (!digits[d]) {
                good = false;
                break;
            }
        }

        if (good) {
            counter++;
        }
    }

    cout << counter << endl;

    return 0;
}
