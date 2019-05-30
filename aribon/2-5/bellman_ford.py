class BellmanFord():
    """ ベルマンフォード法
    重み付き有向グラフにおける単一始点最短路アルゴリズム
    
    * 使用条件
        - DAG（有向グラフで閉路を持たない）であること
        - 負のコストがあってもOK
    
    * 負の閉路がある場合、最短路は求まらないが、負の閉路の検出はできる
    
    * 計算量はO(V*E)
    """
    class Edge():
        """ 重み付き有向辺 """
        def __init__(self, _from, _to, _cost):
            self.from_ = _from
            self.to = _to
            self.cost = _cost
        
    def __init__(self):
        self.edges = []  # 辺
        self.v_set = set()  # 頂点の集合
    
    @property
    def E(self):
        """ 辺数 """
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
        d = [float("inf")] * self.V
        d[s] = 0
    
        while True:
            do_update = False
            for i in range(self.E):
                e = self.edges[i]
                if d[e.from_] != float("inf") and d[e.to] > d[e.from_]+e.cost:
                    d[e.to] = d[e.from_] + e.cost
                    do_update = True
            
            if not do_update: break
        
        return d
    
    def exist_negative_loop(self):
        """ 負の閉路が存在するか否か
        Returns:
            (bool): 負の閉路が存在する(True)/しない(False)
        """
        d = [0] * self.V
        for i in range(self.V):
            for j in range(self.E):
                e = self.edges[j]
                if d[e.to] > d[e.from_] + e.cost:
                    d[e.to] = d[e.from_] + e.cost
                    # n回目にも更新があるなら負の閉路が存在する
                    if i == self.V-1: return True
        return False


def sample1():
    print("---sample1---")

    bf = BellmanFord()
    bf.add(0, 1, 5)
    bf.add(0, 2, 4)
    bf.add(1, 2, -2)
    bf.add(1, 3, 1)
    bf.add(2, 3, 2)
    bf.add(2, 4, 1)
    bf.add(2, 5, 4)
    bf.add(3, 5, 3)
    bf.add(4, 5, 4)

    print(f"bf.exist_negatve_loop(): {bf.exist_negative_loop()}")

    path = bf.shortest_path(0)
    print(f"path: {path}")


def sample2():
    print("---sample2---")

    bf = BellmanFord()
    bf.add(0, 1, 5)
    bf.add(0, 2, 4)
    bf.add(1, 2, -2)
    bf.add(1, 3, 1)
    bf.add(2, 3, 2)
    bf.add(2, 4, 1)
    bf.add(2, 5, 4)
    bf.add(3, 1, -1)
    bf.add(3, 5, 3)
    bf.add(4, 5, 4)

    print(f"bf.exist_negatve_loop(): {bf.exist_negative_loop()}")

    # 負の閉路が存在するので、最短路は求まらない
    #path = bf.shortest_path(0)
    #print(f"path: {path}")


def sample3():
    print("---sample3---")

    bf = BellmanFord()
    bf.add(0, 1, 5)
    bf.add(0, 2, 4)
    bf.add(1, 2, -2)
    bf.add(1, 3, 1)
    bf.add(2, 3, 2)
    bf.add(2, 4, 1)
    bf.add(2, 5, 4)
    bf.add(3, 5, 3)
    bf.add(4, 5, 4)
    bf.add(3, 6, -1)
    bf.add(6, 7, -1)
    bf.add(7, 8, -1)
    bf.add(8, 6, -1)

    print(f"bf.exist_negatve_loop(): {bf.exist_negative_loop()}")
    
    # 負の閉路が存在するので、最短路は求まらない
    #path = bf.shortest_path(0)
    #print(f"path: {path}")


if __name__ == "__main__":
    sample1()
    sample2()
    sample3()
