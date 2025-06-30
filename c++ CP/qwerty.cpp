#include <iostream>
using namespace std;
int main(){
    int the_list;

    for(int i = 0; i < 26; i++){
        cin >> the_list;

        char the_chars = 'a' + the_list - 1;
        cout << the_chars << "";
    }
}