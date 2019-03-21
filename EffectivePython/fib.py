# -*- coding: utf-8 -*-
def fib(n):
    """フィボナッチ数列"""
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(35))
