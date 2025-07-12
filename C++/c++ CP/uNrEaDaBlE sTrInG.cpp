#include <iostream>
using namespace std;
int main(){
    string s;
    cin >> s;

    for(int i = 0; i < s.length(); i++){
        if(i % 2 == 0){
            if(!islower(s[i])){
                cout << "No\n";
                return 0;
            }
        }
        else{
            if(!isupper(s[i])){
                cout << "No\n";
                return 0;
            }
        }
    }

    cout << "Yes" << "\n";
}