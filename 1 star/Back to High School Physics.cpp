#include<iostream>
using namespace std;
int main(){
    int v,t;
    while(cin>>v>>t){
        /*v = at
          a = v/t
          s = at**2/2
          s = 2vt
          */
         int s = 2*v*t;
         cout<<s<<endl;
    }
    return 0;
}