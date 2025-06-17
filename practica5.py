class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1
        return True

def kruskal(graph, nodes, max_spanning=False):
    edges = []
    for u in graph:
        for v, w in graph[u].items():
            edges.append((w, u, v))
    edges.sort(reverse=max_spanning)  # Orden descendente para MaxST
    
    uf = UnionFind(len(nodes))
    mst = []
    total_cost = 0
    
    for w, u, v in edges:
        u_idx = nodes.index(u)
        v_idx = nodes.index(v)
        if uf.union(u_idx, v_idx):
            mst.append((u, v, w))
            total_cost += w
            if len(mst) == len(nodes) - 1:
                break
    return mst, total_cost

# Ejemplo de grafo
graph = {
    'A': {'B': 2, 'D': 6},
    'B': {'A': 2, 'C': 3, 'D': 8},
    'C': {'B': 3, 'D': 4, 'E': 2},
    'D': {'A': 6, 'B': 8, 'C': 4, 'E': 1},
    'E': {'C': 2, 'D': 1}
}
nodes = ['A', 'B', 'C', 'D', 'E']

# Árbol de Mínimo Coste (MST)
mst, min_cost = kruskal(graph, nodes)
print("\nAristas del MST (Kruskal - Mínimo Coste):")
for u, v, w in mst:
    print(f"{u} -- {v} (Peso: {w})")
print(f"Costo total: {min_cost}")

# Árbol de Máximo Coste (MaxST)
maxst, max_cost = kruskal(graph, nodes, max_spanning=True)
print("\nAristas del MaxST (Kruskal - Máximo Coste):")
for u, v, w in maxst:
    print(f"{u} -- {v} (Peso: {w})")
print(f"Costo total: {max_cost}")