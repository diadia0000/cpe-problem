#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    for(int i = 0 ; i<n ;i++){
        int a,b;
        cin>>a;
        cin>>b;
        for(int j = 0 ; j<b ; j++){
            for(int k = 1 ; k<=a ; k++){
                for(int l = 0 ; l<k ; l++){
                    cout<<k;
                }
                cout<<"\n";
            }
            for(int k = a-1 ; k>0 ; k--){
                for(int l = 0 ; l<k ; l++){
                    cout<<k;
                }
                cout<<"\n";
            }
            cout<<"\n";
        }
    }
    return 0;
}