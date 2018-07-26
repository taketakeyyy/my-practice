# -*- coding:utf-8 -*-
import numpy as np
import importlib
nn_mod = importlib.import_module("neural-network")

def test1():
   nn_mod.plot_sigmoid() 

def test2():
    network = nn_mod.init_network()
    x = np.array([1.0, 0.5])
    y = nn_mod.forward(network, x)
    print(y)  # [ 0.31682708  0.69627909]
    
if __name__ == "__main__":
    test1()
    test2()