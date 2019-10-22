# -*- coding:utf-8 -*-


def solve():
    N, W = list(map(int, input().split()))
    Ws, Vs = [], []
    for _ in range(N):
        w, v = list(map(int, input().split()))
        Ws.append(w)
        Vs.append(v)

    memo = [[None for _ in range(W+1)] for __ in range(N+1)]  # メモ化テーブル


    def rec(i, j):
        """i番目以降の品物から重さの総和がj以下となるように選ぶ"""
        if memo[i][j] is not None:
            # すでに調べたことがあるなら、その結果を利用する
            return memo[i][j]

        if i == N:
            # もう品物は残っていない
            res = 0
        elif j < Ws[i]:
            # この品物は入らない
            res = rec(i+1, j)
        else:
            # 入れない場合と入れる場合を両方試す
            res = max(rec(i+1, j), rec(i+1, j-Ws[i])+Vs[i])
        # 結果をメモ化テーブルに記憶する
        memo[i][j] = res
        return res

    ans = rec(0, W)
    print(ans)


if __name__ == "__main__":
    solve()
