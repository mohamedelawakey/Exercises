#include <iostream>
using namespace std;
int main(){
    /*
        1- we enter a number and this number the loob that take numbers rebeteas as this number 
        2- the secound step is put the start and end point 
        3- check if start < end , swap them as a solve
        4- third select the odd numbers add get the sum of it 
    */

    int num, start, end;
    cin >> num;

    for(int i = 0; i < num; i++){
        int sum = 0;
        cin >> start >> end;

        if(start > end){
            swap(start, end);
        }

        for(int j = start + 1; j < end; j++){
            if(j % 2 != 0){
                sum += j;
            }
        }
        cout << sum << "\n";
    }

    return 0;
}