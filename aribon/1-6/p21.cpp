int n, a[MAX_N];

void solve(){
    int ans = 0;

    for(int i=0; i<n; i++){
        for(int j=i+1; j<n; j++){
            for(int k=j+1; k<n; k++){
                int len  = a[i] + a[j] + a[k];  // 周長
                int ma   = max(a[i], max(a[j], a[k]));  // 最も長い棒の長さ
                int rest = len - ma;  // 他の2本の棒の長さの和
                if(ma < rest){
                    ans = max(ans, len);
                }
            }
        }
    }

    printf("%d\n", ans);
}
