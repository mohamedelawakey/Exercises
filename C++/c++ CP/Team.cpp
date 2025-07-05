#include <iostream>
#include <iomanip> 
using namespace std;
int main(){
    int num, n1, n2, n3;
    int counter = 0;
    cin >> num;
    
    for(int i = 0; i < num; i++){
        cin >> n1 >> n2 >> n3;
        if(n1 + n2 + n3 >= 2){
            counter++;
        }
    }
    cout << counter << "\n";
}