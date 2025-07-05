#include <iostream>
#include <algorithm>
#include <cctype>
using namespace std;
int main(){
    int n;
    cin >> n;

    long long a[n];

    for(int i = 0; i < n; i++){
        cin >> a[i];
    }

    int mount = 0, low = 0;

    for (int i = 1; i < n - 1; i++) {
        if (a[i] > a[i - 1] && a[i] > a[i + 1]) {
            mount++;
        } else if (a[i] < a[i - 1] && a[i] < a[i + 1]) {
            low++;
        }
    }

    cout << mount << " " << low << "\n";

}