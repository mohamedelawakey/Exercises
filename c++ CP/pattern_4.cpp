#include <iostream>
#include <cmath> 
using namespace std;
int main(){
    int n;
    cin >> n;

    // up
    for (int i = 1; i <= n; i += 2) {
        for (int j = 1; j <= (n - i) / 2; j++) {
            cout << " ";
        }
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        cout << "\n";
    }

    // low
    for (int i = n - 2; i >= 1; i -= 2) {
        for (int j = 1; j <= (n - i) / 2; j++) {
            cout << " ";
        }
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        cout << "\n";
    }

}