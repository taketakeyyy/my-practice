# -*- coding:utf-8 -*-

def solve():
    N = int(input())
    Ss = list(map(int, input().split()))
    Ts = list(map(int, input().split()))

    itv = []  # 仕事をソートするためのリスト

    # 選べる仕事の中で、最も終了時間が早いものを選ぶことを貪欲的に繰り返す
    for i in range(N):
        itv.append((Ts[i], Ss[i]))
    itv.sort(key= lambda x: x[0])

    # tは最後に選んだ仕事の終了時間
    ans, t = 0, 0
    for i in range(N):
        if t < itv[i][1]:
            ans += 1
            t = itv[i][0]

    print(ans)


if __name__ == "__main__":
    solve()
