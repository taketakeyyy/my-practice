# -*- coding:utf-8 -*-

def is_prime(n):
    """素数判定 O(√N)

    Args:
        n(int): 正の整数
    """
    for i in range(2, n):
        if i*i > n: break
        if n%i == 0: return False
    return n != 1  # 1は素数じゃないので除外


def divisor(n):
    """約数の列挙O(√N)"""
    res = []
    for i in range(1, n):
        if i*i > n: break
        if n%i==0:
            res.append(i)
            if i != n//i: res.append(n//i)
    return res


def prime_factor(n):
    """素因数分解O(√N)"""
    res = []
    for i in range(2, n):
        if i*i > n: break
        while n%i == 0:
            res[i] += 1
            n //= i
    if n!=1: res[n] = 1
    return res








if __name__ == "__main__":
    solve()
