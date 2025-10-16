"""
Atividade A2 - Exercício 1: Componentes Fortemente Conexas
Algoritmo de Kosaraju-Sharir para encontrar componentes fortemente conexas em grafos dirigidos.
Baseado no algoritmo descrito por Cormen et al. (2012).
"""

from graph_utils import DirectedGraph
import sys


def DFS(G):
    """
    DFS de Cormen et al. (2012)
    Chamar a DFS para computar os tempos de término para cada vértice.
    
    Retorna: C (Visitado), T (tempo descoberta), A' (ancestral), F (tempo término)
    """
    vertices = G.get_all_vertices()

    C = {v: False for v in vertices}
    T = {v: float('inf') for v in vertices}
    A = {v: None for v in vertices}
    F = {v: float('inf') for v in vertices}

    # Configurando o tempo de início
    tempo = [0]  # Lista para permitir mutação em função aninhada
    
    # Para cada vértice não visitado
    for u in G.get_all_vertices():
        if C[u] == False:
            DFS_Visit(G, u, C, T, A, F, tempo) # Visita recursivamente os vértices do grafo
    
    return C, T, A, F


def DFS_Visit(G, v, C, T, A, F, tempo):
    """
    DFS-Visit de Cormen et al. (2012)
    Visita recursivamente os vértices do grafo.
    """
    C[v] = True
    tempo[0] = tempo[0] + 1
    T[v] = tempo[0]
    
    # Para cada vizinho de v
    for u in G.vizinhos(v):
        if C[u] == False:
            A[u] = v
            DFS_Visit(G, u, C, T, A, F, tempo)
    
    tempo[0] = tempo[0] + 1
    F[v] = tempo[0]


def DFS_adaptado(G_T, F):
    """
    DFS alterado para que ele execute o laço da linha 6,
    selecionando vértices em ordem decrescente de F (tempo de término).
    
    Retorna: C^T, T^T, A'^T, F^T e a lista de componentes
    """
    vertices = G_T.get_all_vertices()
    
    C = {v: False for v in vertices}
    T = {v: float('inf') for v in vertices}
    A = {v: None for v in vertices}
    F_new = {v: float('inf') for v in vertices}
    
    tempo = [0]
    componentes = []
    
    # Ordena vértices por tempo de término decrescente
    vertices_ordenados = sorted(G_T.get_all_vertices(), key=lambda v: F[v], reverse=True)
    
    # Para cada vértice em ordem decrescente de F
    for u in vertices_ordenados:
        if C[u] == False:
            componente_atual = []
            DFS_Visit_SCC(G_T, u, C, T, A, F_new, tempo, componente_atual)
            componentes.append(sorted(componente_atual))
    
    return C, T, A, F_new, componentes


def DFS_Visit_SCC(G, v, C, T, A, F, tempo, componente):
    """
    DFS-Visit modificado para coletar vértices da componente fortemente conexa.
    """
    C[v] = True
    tempo[0] = tempo[0] + 1
    T[v] = tempo[0]
    componente.append(v)  # Adiciona à componente atual
    
    for u in G.vizinhos(v):
        if C[u] == False:
            A[u] = v
            DFS_Visit_SCC(G, u, C, T, A, F, tempo, componente)
    
    tempo[0] = tempo[0] + 1
    F[v] = tempo[0]


def criar_grafo_transposto(G):
    """
    Cria o grafo transposto G^T (inverte todas as arestas).
    Corresponde às linhas 2-5 do Algoritmo 17.
    """
    G_T = DirectedGraph()
    G_T.vertices = G.vertices.copy()
    G_T.vertex_count = G.vertex_count
    G_T.edge_count = G.edge_count
    
    # A^T ← {} (conjunto vazio de arcos)
    # Para cada (u, v) dentro de A: A^T ← A^T ∪ {(v, u)} -> inverte-se todos os arcos para G^T
    for u in G.get_all_vertices():
        for v in G.vizinhos(u):
            G_T.adjacency_list[v].append(u)
    
    return G_T


def kosaraju_sharir(G):
    """
    Algoritmo de Kosaraju-Sharir
    
    Input: um grafo dirigido não ponderado G = (V, A)
    
    Retorna: A'^T - componentes fortemente conexas
    """
    # Chamar a DFS para computar os tempos de término para cada vértice
    C, T, A_linha, F = DFS(G)

    # Criar grafo transposto    
    G_T = criar_grafo_transposto(G)
    
    # Chamar a DFS alterado para que ele selecione os vértices em ordem decrescente de F
    C_T, T_T, A_T, F_T, componentes = DFS_adaptado(G_T, F)
    
    # Dar saída de cada árvore na floresta em profundidade em A^T como uma
    # componente fortemente conexa
    return componentes


def main():
    if len(sys.argv) < 2:
        print("Uso: python A2_1.py <arquivo_grafo>")
        print("Exemplo: python A2_1.py grafo_dirigido.txt")
        return
    
    arquivo = sys.argv[1]
    
    # Carrega o grafo dirigido
    graph = DirectedGraph()
    graph.ler(arquivo)
    
    # Encontra as componentes fortemente conexas usando Kosaraju-Sharir
    sccs = kosaraju_sharir(graph)
    
    # Imprime as SCCs
    for scc in sccs:
        print('{' + ','.join(map(str, scc)) + '}')


if __name__ == "__main__":
    main()
