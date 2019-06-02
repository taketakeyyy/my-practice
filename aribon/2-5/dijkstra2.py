class Dijkstra():
    """ ダイクストラ法
    重み付きグラフにおける単一始点最短路アルゴリズム

    * 使用条件
        - 負のコストがないこと
        - 有向グラフ、無向グラフともにOK
    
    * 計算量はO(E*log(V))

    * ベルマンフォード法より高速なので、負のコストがないならばこちらを使うとよい
    """        
    def __init__(self, V=None):
        """ 重み付き有向辺 
        無向辺を表現したいときは、_fromと_toを逆にした有向辺を加えればよい

        Args:
            V(int): 頂点数
                    - 頂点数が与えられたときは、すべての辺をINFで初期化する
        """
        self.edges = {}  # edges[(u,v)] = cost := 辺(u,v)のコストcost
        self.v_set = set()  # 頂点の集合

        if V is not None:
            for u in range(V):
                for v in range(V):
                    self.edges[(u,v)] = float("INF")

    @property
    def E(self):
        """ 辺数 
        無向グラフのときは、辺数は有向グラフの倍になる
        """
        return len(self.edges)
    
    @property
    def V(self):
        """ 頂点数 """
        return len(self.v_set)
    
    def add(self, _from, _to, _cost):
        """ 2頂点と、辺のコストを追加する """
        self.edges[(_from, _to)] = _cost
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
                if not (v,i) in self.edges: continue

                cost = self.edges[(v,i)]  # vからiへのコスト
                if d[i] > d[v] + cost:
                    d[i] = d[v] + cost # dの更新
                    heapq.heappush(que, (d[i], i)) # キューに新たな仮の距離の情報をpush
        return d



def sample():
    pass

if __name__ == "__main__":
    sample()
