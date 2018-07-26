#include <iostream>
#include <algorithm>
using namespace std;
static const int MAX = 200000;

/*
[sample input]
6
5
4
1
3
4
3

[sample output]
3
*/
int main(){
    int R[MAX], n;

    // 入力
    cin >> n;
    for(int i=0; i<n; i++){
        cin >> R[i];
    }

    // 実装
    int maxv = -2000000000;  // 十分小さい値
    int minv = R[0];

    for(int i=1; i<n; i++){
        maxv = max(maxv, R[i]-minv);
        minv = min(minv, R[i]);
    }

    cout << maxv << endl;

    return 0;
}