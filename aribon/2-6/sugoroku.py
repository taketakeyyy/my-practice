# -*- coding:utf-8 -*-
"""ユークリッドの互除法を拡張する
"""

def extgcd(a, b, x, y):
    d = a
    if b != 0:
        d = extgcd(b, a%b, y, x)
        y -= (a/b)*x
    else:
        x, y = 1, 0
    return d


def solve():
    a, b = 4, 11
    extgcd(a, b)

if __name__ == "__main__":
    solve()
