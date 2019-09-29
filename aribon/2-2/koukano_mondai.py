# -*- coding:utf-8 -*-
import math


def solve():
    Cs = list(map(int, input().split()))
    A = int(input())

    V = [1,5,10,50,100,500]  # コインの金額

    # 大きな額の硬貨から順番に使い、A円ちょうどを払う
    ans = 0
    for i in range(5, -1, -1):
        t = min(A//V[i], Cs[i])  # コインiを使う枚数
        A -= t * V[i]
        ans += t

    print(ans)


if __name__ == "__main__":
    solve()
