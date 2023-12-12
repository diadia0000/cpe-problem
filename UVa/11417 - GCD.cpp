#include<iostream>
#include<algorithm>
using namespace std;
int GCD(int N){
    long long int G = 0;
    for(int i = 1 ; i<N ; i++){
        for(int j = i+1 ; j<=N ; j++){
            G+=__gcd(i,j);
        }
    }
    return G;
}
int main(){
    int n;
    while(cin>>n){
        if(n == 0)
            break;
        cout<<GCD(n)<<"\n";
    }
    return 0;
}