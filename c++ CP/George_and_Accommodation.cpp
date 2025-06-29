#include <iostream>
#include <iomanip> 
using namespace std;
int main(){
    int n, pi, qi;
    int counter = 0;

    cin >> n;

    for(int i = 0; i < n; i++){
        cin >> pi >> qi;

        if (qi - pi >= 2){
            counter++;
        }
    }
    
    cout << counter << "\n";
}