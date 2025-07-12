#include <iostream>
#include <vector>
using namespace std;
int main(){
    int num;
    cin >> num;

    vector<int> sizee(num);

    for(int i = 0; i < num; i++){
        cin >> sizee[i];
    }

    long long sum = 0;

    for(int i = 0; i < num; i++){
        sum += sizee[i];
    }

    cout << abs(sum) << "\n";
}