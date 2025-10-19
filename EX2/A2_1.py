from graph_utils import DirectedGraph
import sys

def DFS(G):
    """
    Chamar a DFS para computar os tempos de término para cada vértice.

    Retorna: dicionário F com tempos de término de cada vértice
    """
    vertices = G.get_all_vertices()

    C = {v: False for v in vertices}
    A = {v: None for v in vertices}
    F = {v: float('inf') for v in vertices}

    # Configurando o tempo de início
    tempo = [0]
    
    # Para cada vértice não visitado
    for u in G.get_all_vertices():
        if C[u] == False:
            DFS_Visit(G, u, C, A, F, tempo) # Visita recursivamente os vértices do grafo
    
    return F


def DFS_Visit(G, v, C, A, F, tempo):
    """
    Visita recursivamente os vértices do grafo.
    """
    C[v] = True
    
    # Para cada vizinho de v
    for u in G.vizinhos(v):
        if C[u] == False:
            A[u] = v
            DFS_Visit(G, u, C, A, F, tempo)
    
    tempo[0] = tempo[0] + 1
    F[v] = tempo[0]


def DFS_adaptado(G_T, F):
    """
    DFS alterado para que ele execute o laço da linha 6,
    selecionando vértices em ordem decrescente de F (tempo de término).
    
    Retorna: componentes fortemente conexas
    """
    vertices = G_T.get_all_vertices()
    
    C = {v: False for v in vertices}
    componentes = []
    
    # Ordena vértices por tempo de término decrescente
    vertices_ordenados = sorted(G_T.get_all_vertices(), key=lambda v: F[v], reverse=True)
    
    # Para cada vértice em ordem decrescente de F
    for u in vertices_ordenados:
        if C[u] == False:
            componente_atual = []
            DFS_Visit_SCC(G_T, u, C, componente_atual)
            componentes.append(sorted(componente_atual))
    
    return componentes


def DFS_Visit_SCC(G, v, C, componente):
    """
    DFS-Visit modificado para coletar vértices da componente fortemente conexa.
    """
    C[v] = True
    componente.append(v)  # Adiciona à componente atual
    
    for u in G.vizinhos(v):
        if C[u] == False:
            DFS_Visit_SCC(G, u, C, componente)

def criar_grafo_transposto(G):
    """
    Cria o grafo transposto G^T (inverte todas as arestas).
    Corresponde às linhas 2-5 do Algoritmo 17.
    """
    G_T = DirectedGraph()
    G_T.vertices = G.vertices.copy()
    G_T.vertex_count = G.vertex_count
    G_T.edge_count = G.edge_count
    
    # Para cada (u, v) -> (v, u)
    for u in G.get_all_vertices():
        for v in G.vizinhos(u):
            G_T.adjacency_list[v].append(u)
    
    return G_T


def kosaraju_sharir(G):
    """
    Algoritmo de Kosaraju-Sharir
    
    Input: um grafo dirigido não ponderado G = (V, A)
    
    Retorna: lista de componentes fortemente conexas
    """
    # Chamar a DFS para computar os tempos de término para cada vértice
    F = DFS(G)

    # Criar grafo transposto    
    G_T = criar_grafo_transposto(G)
    
    # Chamar a DFS alterado para que ele selecione os vértices em ordem decrescente de F
    componentes = DFS_adaptado(G_T, F)
    
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
        print(','.join(map(str, scc)))


if __name__ == "__main__":
    # TESTE: python .\EX2\A2_1.py .\EX2\test_scc_example.net
    main()