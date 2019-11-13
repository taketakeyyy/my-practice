# -*- coding:utf-8 -*-

def solve():
    # dp[i][j] := s1...si と i1...tjに対するLCSの長さ
    N, M = list(map(int, input().split()))
    s = input()
    t = input()

    dp = [[0 for _ in range(M+1)] for __ in range(N+1)]

    for i in range(0, N):
        for j in range(0, M):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    print(dp[N][M])


if __name__ == "__main__":
    solve()
