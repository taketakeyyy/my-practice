# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    """ ステップ関数
    (例)
    x = np.array([-1.0, 1.0, 2.0])
    y = x > 0         # array([False, True, True], dtype=bool)
    y.astype(np.int)  # array(0, 1, 1)
    """
    y = x > 0
    return y.astype(np.int)

def plot_step_function():
    """ ステップ関数をグラフ化する """
    x = np.arange(-5.0, 5.0, 0.1)
    y = step_function(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)  # y軸の範囲
    plt.show()

def sigmoid(x):
    """ シグモイド関数 """
    return 1 / (1 + np.exp(-x))

def plot_sigmoid():
    """ シグモイド関数をグラフ化する """
    x = np.arange(-5.0, 5.0, 0.1)
    y = sigmoid(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)  # y軸の範囲
    plt.show()
