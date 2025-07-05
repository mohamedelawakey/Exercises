#include <iostream>
#include <iomanip> 
using namespace std;
int main(){
    int w ;
    cin >> w;

    if(w % 2 == 0 && w > 2){
        cout << "YES\n";
    }
    else{
        cout << "NO\n";
    }

}