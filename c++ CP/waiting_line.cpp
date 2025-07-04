#include <iostream>
using namespace std;

int main() {
    int n;
    string s;
    cin >> n >> s;

    string result = "";
    result += s[0];  

    for (int i = 1; i < n; i++) {
        if (s[i] != s[i - 1]) {
            result += s[i];
        }
    }

    cout << result << endl;
    return 0;
}
