# -*- coding:utf-8 -*-
import numpy as np
import importlib
nn_mod = importlib.import_module("neural-network")

def sigmoid_test():
    print("# sigmoid_test")
    nn_mod.plot_sigmoid()

def init_network_test():
    print("# init_network_test")
    network = nn_mod.init_network()
    x = np.array([1.0, 0.5])
    y = nn_mod.forward(network, x)
    print(y)  # [ 0.31682708  0.69627909]

def softmax_test():
    print("# softmax_test")
    a = np.array([0.3, 2.9, 4.0])
    y = nn_mod.softmax(a)
    print(y)
    print(np.sum(y))

def mnist_load_test():
    """ MNISTのロードテスト """
    import sys, os
    sys.path.append(os.pardir)
    from archive.dataset.mnist import load_mnist

    print("# mnist_test")

    # 最初の呼び出しは時間がかかる
    (x_train, t_train), (x_test, t_test) = \
        load_mnist(flatten=True, normalize=False)

    # それぞれのデータの形状を出力
    print(x_train.shape)
    print(t_train.shape)
    print(x_test.shape)
    print(t_test.shape)

def mnist_show_test():
    import sys, os
    sys.path.append(os.pardir)
    import numpy as np
    from archive.dataset.mnist import load_mnist
    from PIL import Image

    def img_show(img):
        pil_img = Image.fromarray(np.uint8(img))
        pil_img.show()

    (x_train, t_train), (x_test, t_test) = \
        load_mnist(flatten=True, normalize=False)

    img = x_train[0]
    label = t_train[0]
    print(label)

    print(img.shape) # (784,)
    img = img.reshape(28, 28) # 形状をもとの画像サイズに変形
    print(img.shape) # (28,28)

    img_show(img)

def neuralnet_mnist_test():
    """ MNISTデータを使って推論処理を行うニューラルネット """
    import sys, os
    sys.path.append(os.pardir)
    import numpy as np
    from archive.dataset.mnist import load_mnist
    from PIL import Image
    import pickle

    def get_data():
        (x_train, t_train), (x_test, t_test) = \
            load_mnist(normalize=True, flatten=True, one_hot_label = False)
        return x_test, t_test

    def init_network():
        """ ネットワークの初期化
        * pickleファイルのsample_wight.pklに保存された
          学習済みの重みパラメータを読み込む
        """
        with open("../archive/ch03/sample_weight.pkl", "rb") as f:
            network = pickle.load(f)
        return network

    def predict(network, x):
        W1, W2, W3 = network["W1"], network["W2"], network["W3"]
        b1, b2, b3 = network["b1"], network["b2"], network["b3"]

        a1 = np.dot(x, W1) + b1
        z1 = nn_mod.sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        z2 = nn_mod.sigmoid(a2)
        a3 = np.dot(z2, W3) + b3
        z3 = nn_mod.sigmoid(a3)

        y = nn_mod.softmax(a3)

        return y

    x, t = get_data()
    network = init_network()

    accuracy_cnt = 0
    for i in range(len(x)):
        y = predict(network, x[i])
        p = np.argmax(y) # 最も確率の高い要素のインデックスを取得
        if p == t[i]:
            accuracy_cnt += 1

    print("Accuracy:" + str(float(accuracy_cnt / len(x))))  # 0.9352

if __name__ == "__main__":
    #sigmoid_test()
    #init_network_test()
    #softmax_test()
    #mnist_test_test()
    #mnist_show_test()
    neuralnet_mnist_test()
