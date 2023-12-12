#include<iostream>
using namespace std;
int main(){
    int n,R;
    while(cin>>n>>R){
        int vol[n] = {0};
        for(int i = 0 ; i<R ; i++){
            int back;
            cin>>back;
            vol[back-1] = 1;
        }
        if(n == R){
            cout<<"*\n";
            continue;
        }

        for(int j = 0 ; j<n ; j++){
            if(vol[j] == 0){
                cout<<j+1<<" ";
            }
        }

        cout<<"\n";
    }
    return 0;
}