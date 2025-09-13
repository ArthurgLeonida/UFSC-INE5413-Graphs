import sys
from collections import defaultdict
from graph_utils import Graph

def buscar_subciclo(graph, start_v, edge_counter):
    """
    Implements Algorithm 8: busca um subciclo e anexa outros encontrados.
    """
    # Linha 1: Inicia o ciclo com o vértice v
    ciclo = [start_v]
    t = start_v  # Linha 2: Armazena o ponto de partida

    # Linhas 3-11: Encontra o primeiro tour fechado
    current_v = start_v
    while True:
        # Encontra uma aresta não visitada conectada a current_v
        next_v = -1
        for neighbor in graph.vizinhos(current_v):
            # Normaliza a aresta (u,v) para u <= v para consistência no contador
            u, v = sorted((current_v, neighbor))
            if edge_counter[(u, v)] > 0:
                next_v = neighbor
                break
        
        # Linha 4-5: Se não há aresta, o tour inicial deve ter terminado.
        # A lógica do pseudocode aqui é um pouco diferente, mas a intenção é a mesma.
        if next_v == -1:
            # Em um grafo euleriano, isso só deve acontecer se não houver mais arestas.
            # O laço principal vai quebrar quando current_v == t
            return False, None # Falha em encontrar um ciclo completo

        # Linha 7-8: Seleciona e "visita" a aresta
        u, v = sorted((current_v, next_v))
        edge_counter[(u, v)] -= 1
        
        # Linha 9-10: Adiciona o vértice ao ciclo e avança
        current_v = next_v
        ciclo.append(current_v)

        # Linha 11: Condição de parada do laço `repeat-until`
        if current_v == t:
            break

    # Linhas 12-16: Procura por vértices no ciclo com arestas não visitadas
    # e anexa os novos subciclos encontrados (splicing)
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
            # Linha 13: Chamada recursiva para encontrar o subciclo (detour)
            success, sub_ciclo = buscar_subciclo(graph, x, edge_counter)
            
            # Linha 14-15: Tratamento de falha
            if not success:
                return False, None
            
            # Linha 16: Anexa o sub_ciclo no ciclo principal (splicing)
            # Ex: ciclo = [a, x, b], sub_ciclo = [x, c, d, x]
            # Novo ciclo = [a, x, c, d, x, b] -> [a, x, c, d, b]
            # O sub_ciclo já começa e termina com 'x', então removemos o último 'x'
            ciclo = ciclo[:i] + sub_ciclo + ciclo[i+1:]
        i += 1
            
    # Linha 17: Retorna sucesso e o ciclo completo
    return True, ciclo

def hierholzer(graph):
    """
    Implements Algorithm 7: O algoritmo principal de Hierholzer.
    """
    # Pré-verificação
    for v in graph.get_all_vertices():
        if graph.grau(v) % 2 != 0:
            return None # Grafo não é Euleriano

    # Linha 1-2: Caso sem arestas
    if graph.qtdArestas() == 0:
        return []

    # Linhas 3-5: Cria e preenche o contador de arestas C
    edge_counter = defaultdict(int)
    for u in graph.get_all_vertices():
        for v in graph.vizinhos(u):
            # Adiciona a aresta apenas uma vez para o par (u,v) com u <= v
            if u < v:
                edge_counter[(u, v)] += 1
    
    # Linha 6: Seleciona um vértice inicial com grau > 0
    start_v = -1
    for v in graph.get_all_vertices():
        if graph.grau(v) > 0:
            start_v = v
            break
            
    if start_v == -1: # Grafo sem arestas
        return [graph.get_all_vertices()[0]] if graph.qtdVertices() > 0 else []

    # Linha 7: Invoca o algoritmo 8 para buscar o ciclo
    success, ciclo = buscar_subciclo(graph, start_v, edge_counter)
    
    # Linha 8-9: Retorna em caso de falha
    if not success:
        return None

    # Linhas 10-14: Verifica se todas as arestas foram usadas
    for count in edge_counter.values():
        if count > 0:
            # Se sobrou alguma aresta, o grafo não era conectado
            return None
    
    return ciclo

def main():
    file_path = sys.argv[1]
    
    g = Graph()
    g.ler(file_path)

    cycle = hierholzer(g) # A lógica principal do algoritmo

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