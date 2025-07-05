#include <iostream>
#include <iomanip> 
using namespace std;
int main(){
    int num1, num2, num3;
    cin >> num1 >> num2 >> num3;
    
    int num_under_1 = 7 - num1;
    int num_under_2 = 7 - num2;
    int num_under_3 = 7 - num3;

    cout << num_under_1 + num_under_2 + num_under_3 << "\n";
}