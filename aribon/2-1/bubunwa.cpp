#include <iostream>
#include <cstdio>
#define MAX_N 20

// input
int a[MAX_N];
int n, k;

// iまででsumを作って、残りi以降を調べる
bool dfs(int i, int sum){
    // n個決め終わったら、今までの和sumがkと等しいかを返す
    if (i == n) return sum == k;

    // a[i]を使わない場合
    if (dfs(i+1, sum)) return true;

    // a[i]を使う場合
    if (dfs(i+1, sum+a[i])) return true;

    // a[i]を使う使わないにかかわらずkが作れないのでfalseを返す
    return false;
}

void solve(){
    if (dfs(0, 0)) printf("Yes\n");
    else printf("No\n");
}