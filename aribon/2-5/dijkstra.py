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
        heapq.heappush(que, (0, s))  # (最短距離, 頂点の番号)をヒープに追加する

        while len(que) != 0:
            prov_cost, v = heapq.heappop(que)  # prov_cost := 暫定的な最短距離
            # キューに格納されている暫定的な最短距離が、現在計算できている最短距離より大きければ、dの更新をする必要はない
            if d[v] < prov_cost: continue

            for i in range(len(self.G[v])):
                # 頂点vに隣接する頂点の最短距離を更新する
                e = self.G[v][i]  # vのi個目の隣接辺e
                if d[e.to] > d[v] + e.cost:
                    d[e.to] = d[v] + e.cost # dの更新
                    heapq.heappush(que, (d[e.to], e.to)) # キューに新たな仮の距離の情報をpush
        return d



def sample():
    V = 10
    djk = Dijkstra(V)
    djk.add(0, 1, 100)
    djk.add(1, 2, 200)
    djk.add(2, 8, 1)
    djk.add(5, 6, 100)

    d = djk.shortest_path(0)

    print(d)
   

if __name__ == "__main__":
    sample()
