# -*- coding:utf-8 -*-


def solve():
    N, W = list(map(int, input().split()))
    Ws, Vs = [], []
    for _ in range(N):
        w, v = list(map(int, input().split()))
        Ws.append(w)
        Vs.append(v)

    dp = [[0 for _ in range(W+1)] for __ in range(N+1)]  # DPテーブル

    for i in range(N-1, -1, -1):
        for j in range(0, W+1):
            if j < Ws[i]:
                # この品物は入らない
                dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i+1][j-Ws[i]]+Vs[i])

    print(dp[0][W])


if __name__ == "__main__":
    solve()
