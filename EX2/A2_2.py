"""
Atividade A2 - Exercício 2: Ordenação Topológica
Algoritmo 20: DFS para Ordenação Topológica
Baseado no algoritmo DFS para ordenação topológica.
Utiliza os rótulos dos vértices na saída.
"""

from graph_utils import DirectedGraph
import sys


def DFS_OT(G):
    """
    Algoritmo 20: DFS para Ordenação Topológica
    
    Input: um grafo dirigido não ponderado G = (V, A)
    
    Retorna: O - lista com os vértices ordenados topologicamente
    """
    # Configurando todos os vértices
    C = {}  # Cor: False = branco (não visitado), True = visitado
    T = {}  # Tempo de início
    F = {}  # Tempo de fim
    
    for v in G.get_all_vertices():
        C[v] = False
        T[v] = float('inf')
        F[v] = float('inf')
    
    # Configurando o tempo de início
    tempo = [0]
    
    # Criando lista com os vértices ordenados topologicamente
    O = []
    
    # Para cada vértice não visitado
    for u in sorted(G.get_all_vertices()):  # Ordena para resultado determinístico
        if C[u] == False:
            # DFS-Visit-OT é especificado no Algoritmo 21
            DFS_Visit_OT(G, u, C, T, F, tempo, O)
    
    # return O
    return O


def DFS_Visit_OT(G, v, C, T, F, tempo, O):
    """
    Algoritmo 21: DFS-Visit-OT
    
    Input: um grafo G = (V, E), vértice de origem v ∈ V,
           e os vetores C, T, e F, e uma variável tempo ∈ Z+, uma lista O
    """
    # C_v ← true
    C[v] = True
    
    # tempo ← tempo + 1
    tempo[0] = tempo[0] + 1
    
    # T_v ← tempo
    T[v] = tempo[0]
    
    # foreach u ∈ N+(v) do
    # Ordena vizinhos para resultado determinístico
    for u in sorted(G.vizinhos(v)):
        # if C_u = false then
        if C[u] == False:
            # DFS-Visit-OT(G, u, C, T, F, tempo, O)
            DFS_Visit_OT(G, u, C, T, F, tempo, O)
    
    # tempo ← tempo + 1
    tempo[0] = tempo[0] + 1
    
    # F_v ← tempo
    F[v] = tempo[0]
    
    # Adiciona o vértice v no início da lista O
    # O ← (v) ∪ O
    O.insert(0, v)


def has_cycle_util(graph, v, visited, rec_stack):
    """
    Função auxiliar para detectar ciclos usando DFS.
    """
    visited.add(v)
    rec_stack.add(v)
    
    for neighbor in graph.vizinhos(v):
        if neighbor not in visited:
            if has_cycle_util(graph, neighbor, visited, rec_stack):
                return True
        elif neighbor in rec_stack:
            return True
    
    rec_stack.remove(v)
    return False


def has_cycle(graph):
    """
    Verifica se o grafo dirigido contém ciclo.
    """
    visited = set()
    rec_stack = set()
    
    for vertex in graph.get_all_vertices():
        if vertex not in visited:
            if has_cycle_util(graph, vertex, visited, rec_stack):
                return True
    
    return False


def main():
    if len(sys.argv) < 2:
        print("Uso: python A2_2.py <arquivo_grafo>")
        print("Exemplo: python A2_2.py grafo_dag.txt")
        return
    
    arquivo = sys.argv[1]
    
    # Carrega o grafo dirigido
    graph = DirectedGraph()
    graph.ler(arquivo)
    
    # Verifica se o grafo é um DAG (não contém ciclos)
    if has_cycle(graph):
        print("Erro: O grafo contém ciclos e não possui ordenação topológica.")
        return
    
    # Realiza a ordenação topológica usando DFS-OT
    topo_order = DFS_OT(graph)
    
    # Imprime a ordem topológica usando os rótulos dos vértices
    labels = [graph.rotulo(v) for v in topo_order]
    print(' , '.join(labels))


if __name__ == "__main__":
    main()
