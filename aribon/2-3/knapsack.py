# -*- coding:utf-8 -*-

def solve():
    N, W = list(map(int, input().split()))
    Ws, Vs = [], []
    for _ in range(N):
        w, v = list(map(int, input().split()))
        Ws.append(w)
        Vs.append(v)

    # dp[i][w] := i番目までの品物から重さの総和がwとなるように選んだときの価値の総和の最大値
    dp = [[None for __ in range(W)] for _ in range(N)]
    dp[0][0] = 0
    dp[0][Ws[0]] = Vs[0]

    for i in range(1, N):
        for w in range(W):
            # 選ぶ場合
            if w+Ws[i] < W and dp[i-1][w] != None:
                dp[i][w+Ws[i]] = max(dp[i-1][w+Ws[i]], dp[i-1][w] + Vs[i])
            # 選ばない場合
            dp[i][w] = dp[i-1][w]

    ans = 0
    for w in range(W):
        ans = max(ans, dp[N-1][w])
    print(ans)

if __name__ == "__main__":
    solve()
