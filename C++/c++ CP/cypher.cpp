#include <iostream>
using namespace std; 

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        int final_digits[100];
        for (int i = 0; i < n; ++i) {
            cin >> final_digits[i];
        }

        for (int i = 0; i < n; ++i) {
            int b_moves_count;
            cin >> b_moves_count; 

            int up_moves = 0;
            int down_moves = 0;

            for (int k = 0; k < b_moves_count; ++k) {
                char move_char;
                cin >> move_char; 
                if (move_char == 'U') {
                    up_moves++;
                } else if (move_char == 'D') {
                    down_moves++;
                }
            }

            int current_final_digit = final_digits[i];
            int original_digit = (current_final_digit - up_moves + down_moves);
            
            original_digit = (original_digit % 10 + 10) % 10;
                
            cout << original_digit;
            if (i < n - 1) {
                cout << " ";
            }
        }
        cout << "\n";
    }

    return 0;
}