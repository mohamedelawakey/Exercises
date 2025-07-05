#include <iostream>
#include <string>
using namespace std;

int main() {
    string input;
    getline(cin, input);  

    int letters[26] = {0};  
    for (int i = 0; i < input.size(); i++) {
        char c = input[i];
        if (c >= 'a' && c <= 'z') {
            letters[c - 'a'] = 1;  
        }
    }

    int count = 0;
    for (int i = 0; i < 26; i++) {
        if (letters[i] == 1) {
            count++;
        }
    }

    cout << count << endl;

    return 0;
}
