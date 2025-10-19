from graph_utils import DirectedGraph
import sys

def DFS_OT(G):
    """    
    Input: um grafo dirigido não ponderado G = (V, A)
    
    Retorna: O - lista com os vértices ordenados topologicamente
    """
    # Configurando todos os vértices
    C = {v: False for v in G.get_all_vertices()}
    O = [] # Lista com os vértices ordenados
    
    # Para cada vértice não visitado
    for u in sorted(G.get_all_vertices()):
        if not C[u]:
            DFS_Visit_OT(G, u, C, O)
    
    # Reverse para obter a ordem topológica correta
    O.reverse()
    return O

def DFS_Visit_OT(G, v, C, O):
    """
    Input: um grafo G = (V, E), um vértice v ∈ V,
    dicionário C (Visitado), lista O (ordem topológica)
    """
    C[v] = True
    
    # Ordena vizinhos para resultado determinístico
    for u in sorted(G.vizinhos(v)):
        if C[u] == False:
            DFS_Visit_OT(G, u, C, O)

    # Adiciona o vértice v no final da lista (será revertida depois)
    O.append(v)

def main():
    if len(sys.argv) < 2:
        print("Uso: python A2_2.py <arquivo_grafo>")
        print("Exemplo: python A2_2.py grafo_dag.txt")
        return
    
    arquivo = sys.argv[1]
    
    # Carrega o grafo dirigido
    graph = DirectedGraph()
    graph.ler(arquivo)
    
    # Realiza a ordenação topológica usando DFS-OT
    topo_order = DFS_OT(graph)
    
    # Imprime a ordem topológica usando os rótulos dos vértices
    labels = [graph.rotulo(v) for v in topo_order]
    print(' , '.join(labels))

if __name__ == "__main__":
    # TESTE: python .\EX2\A2_2.py .\EX2\test_topo.net
    main()
