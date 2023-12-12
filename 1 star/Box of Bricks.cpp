#include <iostream>
using namespace std;
int main(){
    int n,hi;
    int Case = 1;
    while(cin>>n){
        if(n == 0)
            break;
        int block[n];
        int sum = 0;
        for(int i = 0 ; i<n ; i++){
            cin>>block[i];
            sum+=block[i];
        }
        sum /=n;
        int temp = 0;
        for(int j = 0 ; j<n ; j++){
            if(block[j]>sum){
                temp+=block[j]-sum;
            }
        }
        cout<<"Set #"<<Case<<"\n";
        cout<<"The minimum number of moves is "<<temp<<"."<<"\n"<<"\n";
        Case++;
    }
    return 0;
}