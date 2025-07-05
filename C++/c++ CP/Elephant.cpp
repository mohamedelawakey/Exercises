#include <iostream>
#include <iomanip> 
using namespace std;
int main(){
    int num;
    cin >> num;

    int counter = 0;

    for(int i = 5; i >= 1; i--){
        counter += num / i;
        num %= i;
    }

    /*
    we can use this: 
        counter += num / 5;
        num %= 5;

        counter += num / 4;
        num %= 4;

        counter += num / 3;
        num %= 3;

        counter += num / 2;
        num %= 2;

        counter += num / 1;
        num %= 1;
    
    */

    cout << counter << '\n';
}