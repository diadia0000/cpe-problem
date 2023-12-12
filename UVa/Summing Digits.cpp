#include<iostream>
using namespace std;
int digit(int N,int sum){
    sum +=N%10;
    //printf("%d\n",N);
    if(N>=10)
        return digit(N/10,sum);
    if(N<10 and sum>=10)
        return digit(sum,0);
    return sum;

}
int main(){
    long long int n;
    while(cin>>n){
        if(n == 0)
            break;
        if(n<10)
            cout<<n<<endl;
        else
            cout<<digit(n,0)<<endl;
    }
    return 0;
}