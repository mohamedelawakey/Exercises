#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    /*
        1- take a number from use to rebeat and take string from user from 1 to a number
        2- sort the string that user but it
        3- check if there any chars rebeted & check that the sub betwen them != 1
    */
    int num;
    cin >> num;

    while(num--){
        string the_string;
        cin >> the_string;

        sort(the_string.begin(), the_string.end());

        bool is_diverse = true;

        for(int i = 1; i < the_string.size(); i++){
            if(the_string[i] == the_string[i - 1] || the_string[i] - the_string[i - 1] != 1){
                is_diverse = false;
                break;
            }
        }

        if(is_diverse){
            cout << "Yes\n";
        }
        else{
            cout << "No\n";
        }
    }
}