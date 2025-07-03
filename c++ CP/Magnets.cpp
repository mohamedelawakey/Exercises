#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    string current, previous;
    int group_count = 0;

    for (int i = 0; i < n; i++) {
        cin >> current;
        if (i == 0 || current != previous) {
            group_count++;
        }
        previous = current;
    }

    cout << group_count << endl;

    return 0;
}
