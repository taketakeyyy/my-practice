# -*- coding:utf-8 -*-
import sys


def solve():
    """状態数が2^{n+1}程度なので、計算量はO(2^n)"""
    n = int(input())
    As = list(map(int, sys.stdin.readline().split()))
    k = int(input())

    def dfs(i, total):
        if total == k: return True

        if i == len(As): return False

        # As[i]を使う場合
        if dfs(i+1, total+As[i]): return True

        # As[i]を使わない場合
        if dfs(i+1, total): return True

        return False

    if dfs(0, 0):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()
