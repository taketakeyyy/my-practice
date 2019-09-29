# -*- coding:utf-8 -*-
import numpy as np


def solve():
    N, M = list(map(int, input().split()))
    fields = []
    for i in range(N):
        line = list(input())
        fields.append(line)
    fields = np.array(fields)
    print(fields)

    """今いるところを.に書き換える。
    1回のDFSでつながっているWはすべて.に書き換えられるので、
    何回DFSをしたかが答え
    """
    def dfs(y, x):
        fields[y][x] = "."  # 書き換える

        # 移動する8方向をループ
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                nx, ny = x + dx, y + dy

                # nxとnyが庭の範囲内かどうかの判定と、fields[ny][nx]="W"かどうかの判定
                if 0 <= nx < M and 0 <= ny < N and fields[ny][nx] == "W": dfs(ny, nx)

        return

    ans = 0

    for y in range(N):
        for x in range(M):
            if fields[y][x] == "W":
                dfs(y, x)
                ans += 1

    print(ans)


if __name__ == "__main__":
    solve()
