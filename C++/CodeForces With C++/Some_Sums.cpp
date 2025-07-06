#include <iostream>
using namespace std;
int main() {
    int n, a, b;
    cin >> n >> a >> b;
    
    int sum = 0;

    for(int i = 1; i <= n; i++){
        int temp = i;
        int sum_digits = 0;

        while(temp > 0){
            sum_digits += temp % 10;
            temp /= 10;
        }

        if(sum_digits >= a && sum_digits <= b){
            sum += i;
        }
    }
    
    cout << sum << "\n";
}