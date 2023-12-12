#include <iostream>
using namespace std;
int main(){
    int n;
    int Case = 1;
    while (cin >> n){
        int num[n];
        bool flag = false;
        for (int i = 0; i < n; i++){
            cin>>num[i];
            if(num[i]<1)
                flag = true;
        }
        
        int check[10001] = {0};
        int j, k;
        for (int c = 1; c < n; c++){
            if (num[c - 1] >= num[c]){
                flag = true;
                break;
            }
        }
        int cont = 0;
        if (flag == false){
            for (j = 0; j < n; j++){
                for (k = j; k < n; k++){
                    check[cont] = num[j] + num[k];
                    cont += 1;
                }
            }
            for (j = 0; j < cont; j++){
                for (k = j + 1; k < cont; k++){
                    if (check[j] == check[k]){
                        flag = true;
                        break;
                    }
                }
            }
        }
        if (flag)
            cout <<"Case #"<<Case<< ": It is not a B2-Sequence."<<"\n"<<"\n";
        else
            cout <<"Case #"<<Case <<": It is a B2-Sequence."<<"\n"<<"\n";
        Case++;
    }
    return 0;
}