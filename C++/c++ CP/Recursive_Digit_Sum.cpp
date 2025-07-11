#include <iostream>
using namespace std;

long long superDigit(string n, int k = 1) {
    long long sum = 0;
    for (char c : n){
        sum += c - '0';
    } 
    sum *= k;

    if (sum < 10){
        return sum;
    } 
    return superDigit(to_string(sum));
}

int main() {
    string n;
    int k;
    cin >> n >> k;

    cout << superDigit(n, k) << "\n";
    return 0;
}