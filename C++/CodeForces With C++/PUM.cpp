#include <iostream>
using namespace std;
int main() {
    /*
        take a number from user
        reebete the number from 1 to this number but if you find a number can devid with 4 print PUM 
    */
    int num;
    cin >> num;

    for(int i = 1; i <= num * 4; i++){
        if(i % 4 == 0){
            
            cout << "PUM\n";
        }
        else{
            cout << i << " ";
        }
    }
}