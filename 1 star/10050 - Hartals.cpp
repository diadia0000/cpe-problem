#include<iostream>
using namespace std;
int main(){
    int T;
    cin>>T;
    for(int i = 0 ; i<T ; i++){
        int day,P;
        cin>>day>>P;
        int infulday[day+1] = {0};
        int cont = 0;
        for(int j = 0 ; j<P ; j++){
            int temp;
            cin>>temp;
            int week = 7;
            for(int k = 1; k<=day ; k++){
                if(week >7)
                    week = 1;
                if(k%temp == 0 and week!=5 and week!=6)
                    infulday[k] = 1;
                week++;
            }
        }
        for(int l = 1;l<=day ; l++){
            if(infulday[l]==1)
                cont++;
        }
        cout<<cont<<"\n";
    }
    return 0;
}