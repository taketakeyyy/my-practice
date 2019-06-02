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
        """ 重み付き有向辺 
        無向辺を表現したいときは、_fromと_toを逆にした有向辺を加えればよい
        """
        def __init__(self, _from, _to, _cost):
            self.from_ = _from
            self.to = _to
            self.cost = _cost
        
    def __init__(self):
        self.edges = []  # 辺
        self.v_set = set()  # 頂点の集合

    @property
    def E(self):
        """ 辺数 
        無向グラフのときは、辺数が有向グラフの倍になる
        """
        return len(self.edges)
    
    @property
    def V(self):
        """ 頂点数 """
        return len(self.v_set)
    
    def add(self, _from, _to, _cost):
        """ 2頂点と、辺のコストを追加する """
        self.edges.append(self.Edge(_from, _to, _cost))
        self.v_set.add(_from)
        self.v_set.add(_to)
        
    def shortest_path(self, s):
        """ 始点sから頂点iまでの最短路を格納したリストを返す 
        Args:
            s(int): 始点s
        Returns:
            d(list): d[i] := 始点sから頂点iまでの最短路
        """
        import heapq
        que = []  # プライオリティキュー（ヒープ木）
        d = [float("inf")] * self.V
        d[s] = 0
        heapq.heappush(que, (0, s))  # (最短距離, 頂点の番号)をヒープに追加する

        while len(que) != 0:
            prov_cost, v = heapq.heappop(que)
            # キューに格納されている最短距離が、現在計算できている最短距離より大きければ、dの更新をする必要はない
            if d[v] < prov_cost: continue

            # 他の頂点の探索
            for i in range(self.V):
                e = self.edges[v][i]  # vからiへの辺
                if d[e.to] > d[v] + e.cost:
                    d[e.to] = d[v] + e.cost # dの更新
                    heapq.heappush(que, (d[e.to], e.to)) # キューに新たな仮の距離の情報をpush
        return d

    def shortest_path2(self, s):
        """ 始点sから頂点iまでの最短路を格納したリストを返す 
        Args:
            s(int): 始点s
        Returns:
            d(list): d[i] := 始点sから頂点iまでの最短路
        """
        cost = [[float("inf") for i in range(self.V)] for j in range(self.V)]  # cost[u][v] := 辺e=(u,v)のコスト（存在しない場合はINF）
        is_used = [False] * self.V  # 既に使われたかのフラグ
        d = [float("inf")] * self.V
        d[s] = 0

        while True:
            v = -1
            # まだ使われていない頂点のうち距離が最小のものを探す
            for u in range(self.V):
                if not is_used[u] and (v==-1 or d[u] < d[v]): v = u
            
            if v == -1: break
            
            is_used[v] = True

            for u in range(self.V):
                d[u] = min(d[u], d[v]+cost[v][u])


def sample():
    pass

if __name__ == "__main__":
    sample()
