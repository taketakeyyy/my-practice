# -*- coding:utf-8 -*-

def solve():
    N = int(input())
    R = int(input())
    Xs = list(map(int, input().split()))
    Xs.sort()

    i, ans = 0, 0
    while i < N:
        # sはカバーされていない一番左の点の位置
        s = Xs[i]
        i += 1

        # sから距離Rを超える点まで進む
        while i < N and Xs[i] <= s+R: i += 1

        # pは新しく印をつける点の位置
        p = Xs[i-1]

        # pから距離Rを超える点まで進む
        while i < N and Xs[i] <= p+R: i += 1

        ans += 1

    print(ans)


if __name__ == "__main__":
    solve()
