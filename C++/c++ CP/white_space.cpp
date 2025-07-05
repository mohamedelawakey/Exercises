#include <iostream>
using namespace std;
int main(){
    string num;
    cin >> num;

    for(int i = 0; i < num.size(); i++){
        cout << num[i] << " ";
    }
}