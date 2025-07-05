#include <iostream>
using namespace std;
int main(){
    
    int num;
    char c;

    cin >> c ;
    cin >> num;

    for(int i = 0; i < num; i++){
        int nums;
        cin >> nums;
        for(int j = 0; j < nums; j++){
            cout << c;
        }
        cout << "\n";
    }

    return 0;
}