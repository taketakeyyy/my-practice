from gaussian_elimination import gauss_elimination

def gauss_elimination_test():
    A = [[5, -2], [1, 1]]
    b = [5, 8]

    ans = gauss_elimination(A, b)
    print(ans)

gauss_elimination_test()