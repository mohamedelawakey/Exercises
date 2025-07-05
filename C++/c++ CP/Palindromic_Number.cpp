#include <iostream>
using namespace std;
int main(){
    int num;
    cin >> num;

    if(num % 10 == num / 100){
        cout << "Yes\n";
    }
    else{
        cout << "No\n";
    }
}