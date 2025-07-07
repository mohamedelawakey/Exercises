#include <iostream>
using namespace std;
int main(){
    int n;
    cin >> n;

    int total = 0, day = 0;

    while(total < n){
        day++;
        total += day;
    }
    cout << day << "\n";
}