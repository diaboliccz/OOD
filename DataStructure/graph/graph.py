import networkx as nx
import matplotlib.pyplot as plt
class Vertex:
    __slots__ = '_element'
    
    def __init__(self, x):
        self._element = x
    
    def element(self):
        return self._element
    
    def __hash__(self):
        return hash(id(self))

class Edge:
    __slots__ = '_origin', '_destination', '_element'
    
    def __init__(self, u, v, x):
        self._origin = u
        self._destination = v
        self._element = x
    
    def endpoints(self):
        return (self._origin, self._destination)
    
    def opposite(self, v):
        return self._destination if v is self._origin else self._origin
    
    def element(self):
        return self._element
    
    def __hash__(self):
        return hash((self._origin, self._destination))

class Graph:
    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing
    
    def is_directed(self):
        return self._incoming is not self._outgoing
    
    def vertex_count(self):
        return len(self._outgoing)
    
    def vertices(self):
        return self._outgoing.keys()
    
    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2
    
    def edges(self):
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result
    
    def get_edge(self, u, v):
        return self._outgoing[u].get(v)
    
    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])
    
    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge
        
    def insert_vertex(self, x=None):
        v = Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v
    
    def insert_edge(self, u, v, x=None):
        e = Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
    
    def adjacency_list(self):
        return self._outgoing
    
    def adjacency_matrix(self):
        vertices = list(self.vertices())
        n = len(vertices)
        matrix = [[0] * n for i in range(n)]
        for v in vertices:
            for e in self.incident_edges(v):
                u = e.opposite(v)
                matrix[vertices.index(v)][vertices.index(u)] = 1
        return matrix
    
    def draw(self):
        G = nx.Graph()
        for v in self.vertices():
            G.add_node(v.element())
        for e in self.edges():
            G.add_edge(e.endpoints()[0].element(), e.endpoints()[1].element(), label=e.element())
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()
    
    def __str__(self):
        for v in self.vertices():
            print(v.element(), end=' -> ')
            for e in self.incident_edges(v):
                print(e.opposite(v).element() + '(' + str(e.element()) + ')', end=' ')
            print()
    

G = Graph()
u = G.insert_vertex('u')
v = G.insert_vertex('v')
w = G.insert_vertex('w')
z = G.insert_vertex('z')
G.insert_edge(u, v, 'e')
G.insert_edge(u, w, 'g')
G.insert_edge(v, w, 'f')
G.insert_edge(w, z, 'h')
m = G.adjacency_matrix()
G.draw()