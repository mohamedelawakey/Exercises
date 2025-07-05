#include <iostream>
using namespace std;
int main(){
    int num;
    cin >> num;

    int counter = 0;

    counter += num / 100; // add to counter the remender of num after devide it with 100 
    num %= 100; // edit the num to complete calc in the other operation 
    
    counter += num / 20;
    num %= 20;

    counter += num / 10;
    num %= 10;
    
    counter += num / 5;
    num %= 5;

    counter += num / 1;
    num %= 1;

    cout << counter << "\n";
}