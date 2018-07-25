import numpy as np

def AND(x1, x2, bias=-0.7):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    tmp = np.sum(w*x) + bias
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2, bias=0.7):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    tmp = np.sum(x*w) + bias
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2, bias=-0.2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    tmp = np.sum(x*w) + bias
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y  = AND(s1, s2)
    return y
