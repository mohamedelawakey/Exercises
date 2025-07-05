#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    /*

    */
    int n; 
    cin >> n;

    string s; 
    cin >> s;

    int counter0 = 0, counter1 = 0;

    for(char c : s){
        if(c == '0'){
            counter0++;
        }
        else if(c == '1'){
            counter1++;
        }
    }

    if(counter0 == counter1){
        cout << "Good\n";
    }
    else{
        cout << "Bad\n";
    }

}