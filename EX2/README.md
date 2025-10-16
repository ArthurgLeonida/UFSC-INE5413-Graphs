# Atividade A2 - Algoritmos em Grafos

Este diretório contém as implementações para a **Atividade A2** da disciplina de Grafos (INE5413) da UFSC.

## Programas Implementados

### 1. Componentes Fortemente Conexas (A2_1.py)
**Algoritmo:** Kosaraju  
**Entrada:** Grafo dirigido não-ponderado  
**Saída:** Componentes fortemente conexas do grafo

**Uso:**
```bash
python A2_1.py <arquivo_grafo>
```

**Exemplo:**
```bash
python A2_1.py test_scc.txt
```

**Saída esperada:** Cada linha representa uma componente fortemente conexa, com vértices separados por vírgula e entre chaves.

---

### 2. Ordenação Topológica (A2_2.py)
**Algoritmo:** DFS com ordenação topológica  
**Entrada:** Grafo dirigido acíclico (DAG) com vértices rotulados  
**Saída:** Ordenação topológica dos vértices utilizando seus rótulos

**Uso:**
```bash
python A2_2.py <arquivo_grafo>
```

**Exemplo:**
```bash
python A2_2.py test_topo.txt
```

**Saída esperada:** Uma sequência de rótulos separados por vírgula e espaço, representando uma ordenação topológica válida.

---

### 3. Árvore Geradora Mínima (A2_3.py)
**Algoritmo:** Kruskal com Union-Find  
**Entrada:** Grafo não-dirigido ponderado  
**Saída:** Peso total da MST e lista de arestas que a compõem

**Uso:**
```bash
python A2_3.py <arquivo_grafo>
```

**Exemplo:**
```bash
python A2_3.py test_mst.txt
```

**Saída esperada:**
- Primeira linha: peso total da árvore geradora mínima
- Segunda linha: arestas no formato "u-v" separadas por vírgula e espaço

---

## Formato dos Arquivos de Entrada

### Para grafos dirigidos (A2_1.py e A2_2.py):
```
*vertices n
1 rotulo_1
2 rotulo_2
...
n rotulo_n
*arcs
u v
...
```

### Para grafos não-dirigidos ponderados (A2_3.py):
```
*vertices n
1 rotulo_1
2 rotulo_2
...
n rotulo_n
*edges
u v peso
...
```

## Estruturas de Dados Utilizadas

### graph_utils.py
- **DirectedGraph:** Classe para representar grafos dirigidos usando lista de adjacência
- **UndirectedGraph:** Classe para representar grafos não-dirigidos ponderados usando lista de adjacência

### A2_1.py (Kosaraju)
- **Pilha:** Para armazenar vértices em ordem de término da primeira DFS
- **Conjunto (set):** Para marcar vértices visitados
- **Lista de adjacência:** Para representar o grafo transposto

### A2_2.py (Ordenação Topológica)
- **Pilha:** Para construir a ordenação topológica
- **Conjunto (set):** Para marcar vértices visitados e detectar ciclos
- **DFS:** Para explorar o grafo e construir a ordem

### A2_3.py (Kruskal)
- **Union-Find:** Estrutura de dados com path compression e union by rank
- **Lista de arestas ordenadas:** Para processar arestas em ordem crescente de peso
- **Lista:** Para armazenar arestas da MST

## Complexidade

### A2_1.py (Kosaraju)
- **Tempo:** O(V + E) - duas passagens de DFS
- **Espaço:** O(V + E) - para armazenar o grafo transposto

### A2_2.py (Ordenação Topológica)
- **Tempo:** O(V + E) - DFS completa
- **Espaço:** O(V) - pilha e conjunto de visitados

### A2_3.py (Kruskal)
- **Tempo:** O(E log E) - dominado pela ordenação das arestas
- **Espaço:** O(V) - estrutura Union-Find

## Arquivos de Teste

- `test_scc.txt`: Grafo dirigido para testar componentes fortemente conexas
- `test_topo.txt`: Grafo dirigido acíclico para testar ordenação topológica
- `test_mst.txt`: Grafo não-dirigido ponderado para testar MST

## Autores

- Arthur Gislon Leonida
- Matheus Barbieri Munzi
