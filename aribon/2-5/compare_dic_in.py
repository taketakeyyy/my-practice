"""
辞書におけるキーアクセスの速度比較
"""
import time

def sample_in_operator1(dic, N):
    """ in演算子（見つかる） """
    start = time.time()
    for i in range(N):
        if i in dic:
            a = dic[i]
        else:
            a = -1
    end = time.time()

    print(f"sample_in_operator1: {end-start}")


def sample_in_operator2(dic, N):
    """ in演算子（見つからない）"""
    NN = 2 * N
    start = time.time()
    for i in range(N, NN):
        if i in dic:
            a = dic[i]
        else:
            a = -1
    end = time.time()

    print(f"sample_in_operator2: {end-start}")


def sample_try_except1(dic, N):
    """ try except（見つかる） """
    start = time.time()
    for i in range(N):
        try:
            a = dic[i]
        except KeyError:
            a = -1
    end = time.time()

    print(f"sample_try_except1:  {end-start}")


def sample_try_except2(dic, N):
    """ try except（見つからない） """
    NN = N*2
    start = time.time()
    for i in range(N, NN):
        try:
            a = dic[i]
        except KeyError:
            a = -1
    end = time.time()

    print(f"sample_try_except2:  {end-start}")


def sample_get_method1(dic, N):
    """ getメソッド（見つかる） """
    start = time.time()
    for i in range(N):
        a = dic.get(i, -1)
    end = time.time()

    print(f"sample_get_method1:  {end-start}")


def sample_get_method2(dic, N):
    """ getメソッド（見つからない） """
    NN = N*2
    start = time.time()
    for i in range(N, NN):
        a = dic.get(i, -1)
    end = time.time()

    print(f"sample_get_method2:  {end-start}")

if __name__ == "__main__":
    N = 10**8
    dic = {}
    for i in range(N):
        dic[i] = i

    sample_in_operator1(dic, N)
    sample_in_operator2(dic, N)
    sample_try_except1(dic, N)
    sample_try_except2(dic, N)
    sample_get_method1(dic, N)
    sample_get_method2(dic, N)
