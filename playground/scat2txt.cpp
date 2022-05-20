#include <iostream>
#include <fstream>
using namespace std;
int main(){
    string NAME;
    cin >> NAME;
    ifstream file;
    file.open(NAME, ios::in|ios::binary);
    // while(ifs){
    //     string line;
        // getline(ifs, line);

    //     cout<<line<<"\n";
    // }
    char line[100];
    cout<<line<<"\n";
    file.read((char*)&line, 100);
    cout<<line<<"\n";
    file.close();
}