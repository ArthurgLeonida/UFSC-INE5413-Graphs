from collections import defaultdict

class Graph:
    def __init__(self):
        self.vertices = {}  # index -> label
        self.adjacency_list = defaultdict(list)  # vertex -> [(neighbor, weight), ...]
        self.edges = {}  # (u, v) -> weight (for O(1) lookup)
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
        return self.vertices.get(v, "No Key Found")
    
    def vizinhos(self, v):
        """Returns the neighbors of vertex v"""
        return [neighbor for neighbor, _ in self.adjacency_list[v]]
    
    def haAresta(self, u, v):
        """Returns True if edge {u, v} exists, False otherwise"""
        return (u, v) in self.edges or (v, u) in self.edges
    
    def peso(self, u, v):
        """Returns the weight of edge {u, v} if it exists, otherwise infinity"""
        if (u, v) in self.edges:
            return self.edges[(u, v)]
        elif (v, u) in self.edges:
            return self.edges[(v, u)]
        else:
            return float('inf')
    
    def ler(self, arquivo):
        """Load graph from file"""
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
                    self.edges[(u, v)] = weight
                    self.edge_count += 1
                    i += 1
                    
        except FileNotFoundError:
            print(f"Error: File {arquivo} not found")
        except Exception as e:
            print(f"Error reading file: {e}")
    
    def get_all_vertices(self):
        """Helper method to get all vertex indices"""
        return list(self.vertices.keys())