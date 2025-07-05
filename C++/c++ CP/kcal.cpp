#include <iostream>
#include <iomanip> 
using namespace std;
int main(){
    double n1, n2;

    cin >> n1 >> n2;

    double cal = (n1 * n2) / 100;

    cout << fixed << setprecision(6) << cal << "\n";
}