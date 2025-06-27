#include <iostream>
using namespace std;
int main(){
    int a, b;
    cin >> a >> b ;

    int sum = a + b;
    int sub = a - b;
    int mul = a * b;

    int bigest = sum;

    if(sub > bigest){
        bigest = sub;
    }
    if(mul > bigest){
        bigest = mul;
    }

    cout << bigest << "\n";
}