#include <iostream>
#include <cmath> 
using namespace std;
int main(){
    int num;
    cin >> num;

    for(int i = 1; i <= num; i+= 2){
        cout << i << "\n";
        
        /* 

        // we can use it :
            if (i % 2 != 0){
                cout << i << "\n";
            }

        */
    }
}