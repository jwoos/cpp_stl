#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

void sayIt(string aString);

int main() {
    string hi("HI CHLOE!!!");
    
    sayIt(hi);
}

void sayIt(string aString) {
    cout << endl;
    cout << " ";
    for (size_t x = 0; x < aString.size(); x++) {
        cout << aString[x] << " ";
    }
    cout << endl;
    
    for (size_t x = 1; x < aString.size() - 1; x++) {
        cout << " " << aString[x];
        for (size_t y = 1; y < aString.size() * 2 - 2; y++) {
            cout << " ";
        }
        cout << aString[aString.size() - x -1] << endl;
    }
    
    for (int x = aString.size(); x >= 0; x--) {
        cout << aString[x] << " ";
    }
    cout << endl;
}
