#include <iostream>
using namespace std;

long long count_trucks(long long crates, long long loadSize) {
    if (crates <= loadSize)
        return 1;

    long long left = crates / 2;
    long long right = crates - left;

    return count_trucks(left, loadSize) + count_trucks(right, loadSize);
}

int main() {
    long long crates, loadSize;
  
    while (cin >> crates >> loadSize) {
        cout << count_trucks(crates, loadSize) << "\n";
    }

    return 0;
}
