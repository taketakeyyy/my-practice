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

def relu(x):
    """ ReLU関数
    0以上ならxを返し、0未満なら0を返す
    """
    return np.maximum(0, x)  # 入力された値から大きい方を返す

def identity_function(x):
    """ 恒等関数 """
    return x

def init_network():
    """ 重みとバイアスが設定されたディクショナリを返す """
    network = {}
    network["W1"] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network["b1"] = np.array([0.1, 0.2, 0.3])
    network["W2"] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network["b2"] = np.array([0.1, 0.2])
    network["W3"] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network["b3"] = np.array([0.1, 0.2])

    return network

def forward(network, x):
    """ 入力から出力方向への伝達処理 """
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)

    return y

def softmax_old(a):
    """ ソフトマックス関数
    出力層にn個の出力があるとする。
    a := 入力信号
    y{k} := k番目の出力信号
    とすると、ソフトマックス関数は、
    y{k} = exp(a{k})) / sigma{i=1, n}(exp(a{i}))

    [備考]
      * 一個の出力はすべての入力から影響を受ける
      * 指数関数の計算は容易にオーバーフローするので注意
    """
    exp_a = np.exp(a)
    sum_exp_a = np.sum(a)
    y = exp_a / sum_exp_a

    return y

def softmax(a):
    """ 改良版ソフトマックス関数
    オーバーフロー対策をしている
    """
    # 入力信号の中で最も大きい値をcとする
    c = np.max(a)
    exp_a = np.exp(a - c)  # オーバーフロー対策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y
