# -*- coding: utf-8 -*-
import time
from functools import lru_cache

def fact(n):
    """再起処理の練習"""
    if n == 0:
        return 1
    return n * fact(n - 1)

def fib(n):
    """フィボナッチ数列"""
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def fib_memo(n):
    """メモ化フィボナッチ"""
    memo = [0]*(n+1)

    def _fib(n):
        if n <= 1:
            return n
        if memo[n] != 0:
            return memo[n]
        memo[n] = _fib(n-1) + _fib(n-2)
        return memo[n]

    return _fib(n)

@lru_cache()
def fib_lru_cache(n):
    if n == 0:
        return 1
    return fib_lru_cache(n-1) + fib_lru_cache(n-2)


def do_fact():
    print(fact(100))

def do_fib():
    start = time.time()
    print(fib(50))
    stop = time.time()
    print("elapsed: {}".format(stop - start))

def do_fib_memo():
    start = time.time()
    print(fib_memo(50))
    stop = time.time()
    print("elapsed: {}".format(stop - start))

def do_fib_lru_cache():
    start = time.time()
    print(fib_lru_cache(50))
    stop = time.time()
    print("elapsed: {}".format(stop - start))

if __name__ == '__main__':
    #do_fact()
    #do_fib()
    do_fib_memo()
    #do_fib_lru_cache()
