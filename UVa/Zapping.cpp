#include<iostream>
using namespace std;
int main(){
    int a,b;
    while(cin>>a>>b){
        if(a == -1 and b == -1){
            break;
        }
        if(a>b){
            int temp = b;
            b = a;
            a = temp;
        }
        int turn = abs(a-b);
        if(turn>a-b+100){
            turn = a-b+100;
        }
        cout<<turn<<"\n";
    }
    return 0;
}