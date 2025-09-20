import sys
from collections import defaultdict
from graph_utils import Graph

def buscar_subciclo(graph, start_v, edge_counter):
    """
    Busca um subciclo e anexa outros encontrados.
    """
    ciclo = [start_v]
    t = start_v

    # Encontra o primeiro subciclo
    current_v = start_v
    while True:
        next_v = -1
        for neighbor in graph.vizinhos(current_v):
            # Normaliza a aresta (u,v) para u <= v para consistência no contador
            u, v = sorted((current_v, neighbor))
            if edge_counter[(u, v)] > 0:
                next_v = neighbor
                break
        
        if next_v == -1:
            return False, None  # Não há arestas não visitadas, falha

        # Seleciona e visita a aresta
        u, v = sorted((current_v, next_v))
        edge_counter[(u, v)] -= 1
        
        # Adiciona o vértice ao ciclo e avança
        current_v = next_v
        ciclo.append(current_v)

        # Condição de parada do laço
        if current_v == t:
            break

    # Procura por vértices no ciclo com arestas não visitadas
    # e anexa os novos subciclos encontrados
    i = 0
    while i < len(ciclo):
        x = ciclo[i]
        
        # Verifica se o vértice x tem arestas adjacentes não visitadas
        has_unvisited_edges = False
        for neighbor in graph.vizinhos(x):
            u, v = sorted((x, neighbor))
            if edge_counter[(u, v)] > 0:
                has_unvisited_edges = True
                break
        
        if has_unvisited_edges:
            # Chamada recursiva para encontrar o subciclo
            success, sub_ciclo = buscar_subciclo(graph, x, edge_counter)
            
            if not success:
                return False, None
            
            # Anexa o sub_ciclo no ciclo principal
            ciclo = ciclo[:i] + sub_ciclo + ciclo[i+1:]
        i += 1
            
    return True, ciclo

def hierholzer(graph):
    """
    O algoritmo principal de Hierholzer.
    """
    for v in graph.get_all_vertices():
        if graph.grau(v) % 2 != 0:
            return None

    if graph.qtdArestas() == 0:
        return []

    # Cria e preenche o contador de arestas C
    edge_counter = defaultdict(int)
    for u in graph.get_all_vertices():
        for v in graph.vizinhos(u):
            # Adiciona a aresta apenas uma vez para o par (u,v) com u <= v
            if u < v:
                edge_counter[(u, v)] += 1
    
    # Seleciona um vértice inicial com grau > 0
    start_v = -1
    for v in graph.get_all_vertices():
        if graph.grau(v) > 0:
            start_v = v
            break
            
    if start_v == -1: # Grafo sem arestas
        return [graph.get_all_vertices()[0]] if graph.qtdVertices() > 0 else []

    # Buscar o ciclo
    success, ciclo = buscar_subciclo(graph, start_v, edge_counter)
    
    if not success:
        return None

    # Verifica se todas as arestas foram usadas
    for count in edge_counter.values():
        if count > 0:
            # Se sobrou alguma aresta, o grafo não era conectado
            return None
    
    return ciclo

def main():
    file_path = sys.argv[1]
    
    g = Graph()
    g.ler(file_path)

    cycle = hierholzer(g)

    if cycle is not None:
        print("1")
        print(",".join(map(str, cycle)))
    else:
        print("0")

if __name__ == "__main__":
    main()
    # COMANDO PARA TESTAR: python EX1/A1_3.py EX1/ContemCicloEuleriano.net (TEM CICLO)
    # COMANDO PARA TESTAR: python EX1/A1_3.py EX1/ContemCicloEuleriano2.net (TEM CICLO)
    # COMANDO PARA TESTAR: python EX1/A1_3.py EX1/SemCicloEuleriano.net (SEM CICLO)