#include<bits/stdc++.h>
using namespace std;
int main(){
    int h1, m1, h2, m2;
    while (cin >> h1 >> m1 >> h2 >> m2){
        if(h1==0 & h2==0 & m1==0 &m2==0)
            break;
        int ans = 0;
        while (1){
            if (h1==h2 and m1==m2)
                break;
            m1++;
            ans++;
            if (m1 == 60){
                m1 = 0;
                h1++;
            }
            if (h1 == 24){
                h1 = 0;
            }
        }
        cout << ans << "\n";
    }
}