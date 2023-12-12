#include<iostream>
using namespace std;
int main(){
	int n;
	int Case = 1;
	cin>>n;
	for(int i = 0 ; i<n ; i++){
		int a,b;
		cin>>a;
        cin>>b;
		int odd = 0;
		for(int j = min(a,b) ; j<=max(a,b) ; j++){
			if(j%2 !=0)
				odd+=j;
		}
		cout<<"Case "<<Case<<": "<<odd<<"\n";
		Case++;
	}
	return 0;
}
