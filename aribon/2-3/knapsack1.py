# -*- coding:utf-8 -*-


def solve():
    N, W = list(map(int, input().split()))
    Ws, Vs = [], []
    for _ in range(N):
        w, v = list(map(int, input().split()))
        Ws.append(w)
        Vs.append(v)

    def rec(i, j):
        """i番目以降の品物から重さの総和がj以下となるように選ぶ"""
        if i == N:
            # もう品物は残っていない
            res = 0
        elif j < Ws[i]:
            # この品物は入らない
            res = rec(i+1, j)
        else:
            # 入れない場合と入れる場合を両方試す
            res = max(rec(i+1, j), rec(i+1, j-Ws[i])+Vs[i])
        return res

    ans = rec(0, W)
    print(ans)


if __name__ == "__main__":
    solve()
