#include <iostream>
using namespace std;
int main(){
    int n ;
    cin >> n;

    long long the_list[100001];
    long long sum_the_list = 0;
    for(int i = 0; i < n; i++){
        cin >> the_list[i];
        sum_the_list += the_list[i];
    }

    long long x;
    cin >> x;

    long long full_copies = x / sum_the_list;
    long long current_sum = full_copies * sum_the_list;
    long long count = full_copies * n;

    for (int i = 0; i < n; ++i) {
        current_sum += the_list[i];
        count++;
        if (current_sum > x){
            break;
        } 
    }
    cout << count << "\n";
     
}