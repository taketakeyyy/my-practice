class Dijkstra():
    """ ダイクストラ法
    重み付きグラフにおける単一始点最短路アルゴリズム

    * 使用条件
        - 負のコストがないこと
        - 有向グラフ、無向グラフともにOK
    
    * 計算量はO(E*log(V))

    * ベルマンフォード法より高速なので、負のコストがないならばこちらを使うとよい
    """
    class Edge():
        """ 重み付き有向辺 """
        def __init__(self, _to, _cost):
            self.to = _to
            self.cost = _cost

    def __init__(self, V):
        """ 重み付き有向辺
        無向辺を表現したいときは、_fromと_toを逆にした有向辺を加えればよい

        Args:
            V(int): 頂点の数
        """
        self.G = [[] for i in range(V)]  # 隣接リストG[u][i] := 頂点uのi個目の隣接辺
        self._E = 0  # 辺の数
        self._V = V  # 頂点の数

    @property
    def E(self):
        """ 辺数
        無向グラフのときは、辺数は有向グラフの倍になる
        """
        return self._E
    
    @property
    def V(self):
        """ 頂点数 """
        return self._V
    
    def add(self, _from, _to, _cost):
        """ 2頂点と、辺のコストを追加する """
        self.G[_from].append(self.Edge(_to, _cost))
        self._E += 1
        
    def shortest_path(self, s):
        """ 始点sから頂点iまでの最短路を格納したリストを返す 
        Args:
            s(int): 始点s
        Returns:
            d(list): d[i] := 始点sから頂点iまでの最短コストを格納したリスト。
                     到達不可の場合、値はfloat("inf")
        """
        import heapq
        que = []  # プライオリティキュー（ヒープ木）
        d = [float("inf")] * self.V
        d[s] = 0
        heapq.heappush(que, (0, s))  # 始点の(最短距離, 頂点番号)をヒープに追加する

        while len(que) != 0:
            cost, v = heapq.heappop(que)
            # キューに格納されている最短経路の候補がdの距離よりも大きければ、他の経路で最短経路が存在するので、処理をスキップ
            if d[v] < cost: continue

            for i in range(len(self.G[v])):
                # 頂点vに隣接する各頂点に関して、頂点vを経由した場合の距離を計算し、今までの距離(d)よりも小さければ更新する
                e = self.G[v][i]  # vのi個目の隣接辺e
                if d[e.to] > d[v] + e.cost:
                    d[e.to] = d[v] + e.cost  # dの更新
                    heapq.heappush(que, (d[e.to], e.to))  # キューに新たな最短経路の候補(最短距離, 頂点番号)の情報をpush
        return d



def sample1():
    # 有向グラフの最短路を求める例
    V = 10
    djk = Dijkstra(V)
    djk.add(0, 1, 100)
    djk.add(1, 2, 200)
    djk.add(2, 8, 1)
    djk.add(5, 6, 100)

    d = djk.shortest_path(1)
    print(d)
    # [inf, 0, 200, inf, inf, inf, inf, inf, 201, inf]
   

def sample2():
    # 無向グラフの最短路を求める例
    # https://nw.tsuda.ac.jp/lec/dijkstra/
    # 上記のサイトの例のグラフの最短路を求める
    V = 8
    djk = Dijkstra(V)
    # 無向辺の場合、両方の向きの有向辺を加える
    djk.add(0,1,1)
    djk.add(1,0,1)

    djk.add(0,2,7)
    djk.add(2,0,7)

    djk.add(0,3,2)
    djk.add(3,0,2)

    djk.add(1,4,2)
    djk.add(4,1,2)

    djk.add(1,5,4)
    djk.add(5,1,4)

    djk.add(2,5,2)
    djk.add(5,2,2)

    djk.add(2,6,3)
    djk.add(6,2,3)

    djk.add(3,6,5)
    djk.add(6,3,5)

    djk.add(4,5,1)
    djk.add(5,4,1)

    djk.add(5,7,6)
    djk.add(7,5,6)

    djk.add(6,7,2)
    djk.add(7,6,2)

    d = djk.shortest_path(0)
    print(d)
    # [0, 1, 6, 2, 3, 4, 7, 9]

if __name__ == "__main__":
    sample1()
    sample2()
