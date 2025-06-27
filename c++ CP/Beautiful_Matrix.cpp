#include <iostream>
using namespace std;

int main() {
    int x;
    int row = 0, col = 0;

    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= 5; j++) {
            cin >> x;
            if (x == 1) {
                row = i;
                col = j;
            }
        }
    }

    int row_diff = row - 3;
    if (row_diff < 0) row_diff = - row_diff;

    int col_diff = col - 3;
    if (col_diff < 0) col_diff = - col_diff;

    int the_move = row_diff + col_diff;
    cout << the_move << "\n";

    return 0;
}
