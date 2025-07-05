#include <iostream>
#include <cmath> 
using namespace std;
int main(){
    int x, y, z, temp1, temp2;
    cin >> x >> y >> z;
    
    temp1 = x;
    x = y;
    y = temp1; // 2

    temp2 = x;
    x = z;
    z = temp2;
    
    cout << x << " " << y << " " << z << "\n";
}