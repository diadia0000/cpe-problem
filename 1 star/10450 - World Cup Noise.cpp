#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int count = 0;
    for(int i = 0 ; i<n ; i++){
        long long int temp;
        cin>>temp;
        long long int num[temp+2]; // wrong answer
        num[0] = 1;
        num[1] = 1;  
        for(long long int j = 1 ; j<temp+1 ; j++){
            num[j+1] = num[j]+num[j-1];
        }
        count+=1;
        cout<<"Scenario #"<<count<<":\n"<<num[temp+1]<<"\n\n";
    }
    // 我明天會去問教授....
}