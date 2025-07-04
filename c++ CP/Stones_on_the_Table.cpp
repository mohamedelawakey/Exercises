#include <iostream>
using namespace std;

int main() {
    int n;
    string s;
    cin >> n >> s;

    int removeCount = 0;

    for (int i = 1; i < n; i++) {
        if (s[i] == s[i - 1]) {
            removeCount++;
        }
    }

    cout << removeCount << endl;
    return 0;
}
