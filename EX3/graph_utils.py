from collections import defaultdict, deque

class DirectedWeightedGraph:
    """Class to represent a directed weighted graph (for flow algorithms)"""
    def __init__(self):
        self.vertices = {}  # index -> label
        self.adjacency_list = defaultdict(list)  # vertex -> [(neighbor, capacity), ...]
        self.capacity = {}  # (u, v) -> capacity
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
        return [neighbor for neighbor, _ in self.adjacency_list[v]]
    
    def capacidade(self, u, v):
        """Returns the capacity of edge (u, v)"""
        return self.capacity.get((u, v), 0)
    
    def ler(self, arquivo):
        """Load directed weighted graph from file"""
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
            
            # Read edges section (directed arcs with weights/capacities)
            if i < len(lines) and lines[i] == '*arcs':
                i += 1
                while i < len(lines):
                    parts = lines[i].split()
                    u = int(parts[0])
                    v = int(parts[1])
                    cap = float(parts[2]) if len(parts) > 2 else 1.0
                    
                    # Add directed edge u -> v with capacity
                    self.adjacency_list[u].append((v, cap))
                    self.capacity[(u, v)] = cap
                    self.edge_count += 1
                    i += 1
                    
        except FileNotFoundError:
            print(f"Error: File {arquivo} not found")
        except Exception as e:
            print(f"Error reading file: {e}")
    
    def get_all_vertices(self):
        """Helper method to get all vertex indices"""
        return list(self.vertices.keys())


class BipartiteGraph:
    """Class to represent a bipartite graph (for Hopcroft-Karp)"""
    def __init__(self):
        self.vertices = {}  # index -> label
        self.adjacency_list = defaultdict(list)  # vertex -> [neighbors]
        self.partition1 = []  # First partition
        self.partition2 = []  # Second partition
        self.vertex_count = 0
        self.edge_count = 0
    
    def qtdVertices(self):
        """Returns the number of vertices"""
        return self.vertex_count
    
    def qtdArestas(self):
        """Returns the number of edges"""
        return self.edge_count
    
    def rotulo(self, v):
        """Returns the label of vertex v"""
        return self.vertices.get(v, "No Key Found")
    
    def vizinhos(self, v):
        """Returns the neighbors of vertex v"""
        return self.adjacency_list[v]
    
    def ler(self, arquivo):
        """Load bipartite graph from file"""
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
                    
                    # Add edge (undirected for bipartite)
                    self.adjacency_list[u].append(v)
                    self.adjacency_list[v].append(u)
                    self.edge_count += 1
                    i += 1
                    
        except FileNotFoundError:
            print(f"Error: File {arquivo} not found")
        except Exception as e:
            print(f"Error reading file: {e}")
    
    def set_bipartition(self, partition1, partition2):
        """Set the two partitions of the bipartite graph"""
        self.partition1 = partition1
        self.partition2 = partition2
    
    def get_all_vertices(self):
        """Helper method to get all vertex indices"""
        return list(self.vertices.keys())


class UndirectedGraph:
    """Class to represent an undirected graph (for coloring)"""
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
        """Returns the degree of vertex v"""
        return len(self.adjacency_list[v])
    
    def rotulo(self, v):
        """Returns the label of vertex v"""
        return self.vertices.get(v, "No Key Found")
    
    def vizinhos(self, v):
        """Returns the neighbors of vertex v"""
        return self.adjacency_list[v]
    
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
                    
                    # Add edge (undirected)
                    self.adjacency_list[u].append(v)
                    self.adjacency_list[v].append(u)
                    self.edge_count += 1
                    i += 1
                    
        except FileNotFoundError:
            print(f"Error: File {arquivo} not found")
        except Exception as e:
            print(f"Error reading file: {e}")
    
    def get_all_vertices(self):
        """Helper method to get all vertex indices"""
        return list(self.vertices.keys())
