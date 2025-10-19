from collections import defaultdict

class DirectedGraph:
    """Class to represent a directed graph (for SCC and Topological Sort)"""
    def __init__(self):
        self.vertices = {}  # index -> label
        self.adjacency_list = defaultdict(list)  # vertex -> [neighbors]
        self.vertex_count = 0
        self.edge_count = 0
    
    def qtdVertices(self):
        """Returns the number of vertices"""
        return self.vertex_count
    
    def qtdArestas(self):
        """Returns the number of edges"""
        return self.edge_count
    
    def grau(self, v):
        """Returns the out-degree of vertex v"""
        return len(self.adjacency_list[v])
    
    def rotulo(self, v):
        """Returns the label of vertex v"""
        return self.vertices.get(v, "No Key Found")
    
    def vizinhos(self, v):
        """Returns the neighbors (out-edges) of vertex v"""
        return self.adjacency_list[v]
    
    def ler(self, arquivo):
        """Load directed graph from file"""
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f.readlines() if line.strip()]
            
            i = 0
            # Read vertices section
            if lines[i].startswith('*vertices'):
                n = int(lines[i].split()[1])
                self.vertex_count = n
                i += 1
                
                # Read vertex labels
                for j in range(n):
                    parts = lines[i + j].split(None, 1)
                    vertex_id = int(parts[0])
                    label = parts[1] if len(parts) > 1 else str(vertex_id)
                    self.vertices[vertex_id] = label
                
                i += n
            
            # Read edges section (directed arcs)
            if i < len(lines) and lines[i] == '*arcs':
                i += 1
                while i < len(lines):
                    parts = lines[i].split()
                    u = int(parts[0])
                    v = int(parts[1])
                    
                    # Add directed edge u -> v
                    self.adjacency_list[u].append(v)
                    self.edge_count += 1
                    i += 1
                    
        except FileNotFoundError:
            print(f"Error: File {arquivo} not found")
        except Exception as e:
            print(f"Error reading file: {e}")
    
    def get_all_vertices(self):
        """Helper method to get all vertex indices"""
        return list(self.vertices.keys())

class UndirectedGraph:
    """Class to represent an undirected weighted graph (for MST algorithms)"""
    def __init__(self):
        self.vertices = {}  # index -> label
        self.adjacency_list = defaultdict(list)  # vertex -> [(neighbor, weight), ...]
        self.edges = []  # list of (u, v, weight) for all edges
        self.vertex_count = 0
        self.edge_count = 0
    
    def qtdVertices(self):
        """Returns the number of vertices"""
        return self.vertex_count
    
    def qtdArestas(self):
        """Returns the number of edges"""
        return self.edge_count
    
    def grau(self, v):
        """Returns the degree of vertex v"""
        return len(self.adjacency_list[v])
    
    def rotulo(self, v):
        """Returns the label of vertex v"""
        return self.vertices.get(v, "No Key Found")
    
    def vizinhos(self, v):
        """Returns the neighbors of vertex v"""
        return [neighbor for neighbor, _ in self.adjacency_list[v]]
    
    def peso(self, u, v):
        """Returns the weight of edge {u, v} if it exists, otherwise infinity"""
        for neighbor, weight in self.adjacency_list[u]:
            if neighbor == v:
                return weight
        return float('inf')
    
    def ler(self, arquivo):
        """Load undirected graph from file"""
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f.readlines() if line.strip()]
            
            i = 0
            # Read vertices section
            if lines[i].startswith('*vertices'):
                n = int(lines[i].split()[1])
                self.vertex_count = n
                i += 1
                
                # Read vertex labels
                for j in range(n):
                    parts = lines[i + j].split(None, 1)
                    vertex_id = int(parts[0])
                    label = parts[1] if len(parts) > 1 else str(vertex_id)
                    self.vertices[vertex_id] = label
                
                i += n
            
            # Read edges section
            if i < len(lines) and lines[i] == '*edges':
                i += 1
                while i < len(lines):
                    parts = lines[i].split()
                    u = int(parts[0])
                    v = int(parts[1])
                    weight = float(parts[2]) if len(parts) > 2 else 1.0
                    
                    # Add edge (undirected)
                    self.adjacency_list[u].append((v, weight))
                    self.adjacency_list[v].append((u, weight))
                    self.edges.append((u, v, weight))
                    self.edge_count += 1
                    i += 1
                    
        except FileNotFoundError:
            print(f"Error: File {arquivo} not found")
        except Exception as e:
            print(f"Error reading file: {e}")
    
    def get_all_vertices(self):
        """Helper method to get all vertex indices"""
        return list(self.vertices.keys())

class UnionFind:
    """
    Implementation of the Union-Find (Disjoint Set Union - DSU) data structure
    with Path Compression and Union by Rank optimizations.
    """

    def __init__(self, elementos):
        """
        Constructor: Initializes the Union-Find with the given elements.
        """
        # Dictionary that maps each element to its parent.
        # Initially, each element is its own parent (root of its own tree).
        self.parent = {elem: elem for elem in elementos}

        # Dictionary that maps each element to its rank.
        # Initially, all elements have rank 0.
        self.rank = {elem: 0 for elem in elementos}

    def encontra(self, elemento):
        """
        Find with Path Compression: finds the root of the set containing 'elemento'.
        """
        # If the element is not the root of its tree (its parent is not itself)
        if self.parent[elemento] != elemento:
            # Recursively find the root and compress the path
            self.parent[elemento] = self.encontra(self.parent[elemento])
        
        return self.parent[elemento]

    def uniao(self, elemento1, elemento2):
        """
        Union by Rank: unites the sets containing 'elemento1' and 'elemento2'.
        Returns True if a union was performed, False if they were already in the same set.
        """
        # Find the roots of the two sets.
        raiz1 = self.encontra(elemento1)
        raiz2 = self.encontra(elemento2)

        # if both elements have the same root, they are already in the same set.
        if raiz1 == raiz2:
            return False

        # Union by Rank: attaches the tree of lower rank to the tree of higher rank.
        if self.rank[raiz1] > self.rank[raiz2]:
            self.parent[raiz2] = raiz1
        elif self.rank[raiz2] > self.rank[raiz1]:
            self.parent[raiz1] = raiz2
        else:
            # If ranks are equal, make one root the parent of the other and increase its rank.
            self.parent[raiz2] = raiz1
            self.rank[raiz1] += 1
        
        return True