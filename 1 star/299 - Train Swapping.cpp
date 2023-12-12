#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    for(int i = 0 ; i<n ; i++){
        int L;
        cin>>L;
        int train[L];
        for(int j = 0 ; j<L ; j++){
            cin>>train[j];
        }
        int count = 0;
        // bubble sort
        for(int k = 0 ; k<L ; k++){
            for(int l = k ; l<L ; l++){
                if(train[k]>train[l]){
                    int temp = train[k];
                    train[k] = train[l];
                    train[l] = temp;
                    count++;
                }
            }
        }
        cout<<"Optimal train swapping takes "<<count<<" swaps.\n";
    }
    return 0;
}