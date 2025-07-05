#include <iostream>
#include <iomanip> 
using namespace std;
int main(){
    int counter = 0;
    int totalCubes = 0;
    int num;

    cin >> num;

    for(int i = 1; ; i++){
        int need = i * (i + 1) / 2;
        if(totalCubes + need <= num){
            totalCubes += need;
            counter++;
        }
        else{
            break;
        }
    }
    cout << counter << "\n";
}