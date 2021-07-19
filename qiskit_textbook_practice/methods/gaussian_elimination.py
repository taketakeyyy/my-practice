from sympy import Matrix

def gauss_elimination(A, b):
    """ガウスの消去法で、解を返す
    参考：https://atatat.hatenablog.com/entry/sympy11_matrix_calc
    """
    all_zero = True
    for x in b:
        if x != 0:
            all_zero = False
            break

    AA = A
    if not all_zero:
        # 拡大係数行列にする
        for i in range(len(b)):
            AA[i].append(b[i])
    M = Matrix(AA)

    Mrref = M.rref()  # 階段行列にする（すると、右列が解になる）
    nrow = Mrref[0].shape[0]
    # print(Mrref[0])

    ans = []
    for i in range(nrow):
        ans.append(Mrref[0][i, -1])
    return ans
