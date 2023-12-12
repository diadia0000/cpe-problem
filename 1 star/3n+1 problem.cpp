#include<iostream>
using namespace std;
int main(){
    int i,j;
    while(cin>>i>>j){
        int Maxcycle = -1;
        for(int k = min(i,j) ; k<=max(i,j) ; k++){
            int temp = k;
            int cycle = 1;
            while(temp!=1){
                if(temp%2 == 0){
                    temp/=2;
                }else{
                    temp = temp*3+1;
                }
                cycle++;
            }
            Maxcycle = max(cycle,Maxcycle);
        }
        cout<<i<<" "<<j<<" "<<Maxcycle<<endl;
    }
}