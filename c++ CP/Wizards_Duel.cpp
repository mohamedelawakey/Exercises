#include <iostream>
#include <iomanip> 
using namespace std;
int main(){
    double length, harry, Voldemort;
    cin >> length >> harry >> Voldemort;
    
    double result = (length * harry) / (harry + Voldemort);
    cout << result << "\n";
}