#include <iostream>
#include <algorithm>
#include <cctype>
using namespace std;
int main(){
    int n; 
    cin >> n;

    static long long the_list[1000000];

    for(int i = 0; i < n; i++){
        cin >> the_list[i];
    }

    long long the_max = the_list[0];
    long long the_min = the_list[0];
    
    for(int i = 1; i < n; i++){
        if(the_list[i] > the_max){
            the_max = the_list[i];
        }
        if(the_list[i] < the_min){
            the_min = the_list[i];
        }
    }

    cout << the_max << " " << the_min << "\n";
}