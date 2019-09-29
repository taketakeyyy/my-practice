# -*- coding:utf-8 -*-
import sys
import numpy as np
import queue


def solve():
    N, M = list(map(int, sys.stdin.readline().split()))
    meiro = []
    for i in range(N):
        line = list(input())
        meiro.append(line)
    meiro = np.array(meiro)

    # 各点までの最短距離の配列
    d = [[float("inf") for _ in range(M)] for __ in range(N)]  # 初期値はINF

    # 移動4方向のベクトル
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # スタート地点とゴール地点の座標を取得する
    for y in range(M):
        for x in range(N):
            if meiro[y][x] == "S": sy, sx = y, x
            if meiro[y][x] == "G": gy, gx = y, x


    def bfs():
        """(sx, sy)から(gx, gy)への最短路を求める
        たどり着けないとINF
        """
        que = queue.Queue()
        que.put((sy, sx))  # スタート地点をキューに入れる
        d[sy][sx] = 0      # スタート地点の距離は0

        # キューが空になるまで幅優先探索でループする
        while not que.empty():
            # キューの先頭を取り出す
            y, x = que.get()

            # 取り出した地点がゴール地点なら探索をやめる
            if y == gy and x == gx: break

            # 移動4方向をループ
            for i in range(4):
                # 移動した後の点をnx, ny とする
                ny, nx = y + dy[i], x + dx[i]

                # 移動が可能かの判定と、すでに訪れたことがあるかの判定（d[ny][nx] != INFなら訪れたことある）
                if 0 <= ny < M and 0 <= nx < N and meiro[ny][nx] != "#" and d[ny][nx] == float("inf"):
                    # 移動できるならキューに入れ、その点の距離を(x,y)からの距離+1で確定する
                    que.put((ny, nx))
                    d[ny][nx] = d[y][x] + 1
        return d[gy][gx]

    ans = bfs()
    print(ans)


if __name__ == "__main__":
    solve()
