#include <iostream>
using namespace std;

int sum(int arr[], int i, int n) {
    if (i == n) return 0;
    return arr[i] + sum(arr, i + 1, n);
}

int main() {
    int x;
    cin >> x;

    for (int i = 1; i <= x; i++) {
        int N;
        cin >> N;
        int arr[100];
        for (int j = 0; j < N; j++) {
            cin >> arr[j];
        }
        cout << "Case " << i << ": " << sum(arr, 0, N) << endl;
    }

    return 0;
}
