#include <iostream>
#include <iomanip> 
using namespace std;
int main(){
    int a,b;

    cin >> a >> b;

    double a_b_3 = (a - b) / 3.0;
    double c = a_b_3 + b ;

    if(c == int(c)){
        cout << (int)c << "\n";
    }
    else{
        cout << fixed << setprecision(7) << c << "\n";
    }
}