#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int min_price = -1;

    for (int i = 0; i < n; i++) {
        int a, p, x;
        cin >> a >> p >> x;

        if (x > a) { 
            if (min_price == -1 || p < min_price) {
                min_price = p;
            }
        }
    }

    cout << min_price << endl;
    return 0;
}
