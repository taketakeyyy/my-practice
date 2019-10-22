# -*- coding:utf-8 -*-


def solve():
    N, W = list(map(int, input().split()))
    Ws, Vs = [], []
    for _ in range(N):
        w, v = list(map(int, input().split()))
        Ws.append(w)
        Vs.append(v)

    # DP[i+1][j] := i番目までの品物から重さの総和がj以下となるように選んだときの価値の総和の最大値
    dp = [[0 for _ in range(W+1)] for __ in range(N+1)]  # DPテーブル

    for i in range(0, N):
        for j in range(0, W+1):
            if j < Ws[i]:
                # この品物は入らない
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-Ws[i]]+Vs[i])

    print(dp[N][W])


if __name__ == "__main__":
    solve()
