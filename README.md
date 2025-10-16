# Graph Project - INE5413

This repository contains the implementations for Practical Activities of the Graphs (INE5413) discipline at the Federal University of Santa Catarina (UFSC), taught by Prof. Rafael de Santiago.

## Project Objective

The project aims to create a graph library and implement fundamental algorithms for the analysis and solution of problems in un-directed, weighted graphs.

## Implemented Features

The following features were developed for **Activity A1 (EX1)**:

* **1. Representation (2.0 pts):** A class to represent an un-directed, weighted graph, with methods for essential operations such as counting vertices and edges, a vertex's degree, and checking for edges.

* **2. Searches (2.0 pts):** Implementation of the Breadth-First Search (BFS) algorithm, which organizes vertices by level starting from an initial vertex.

* **3. Eulerian Cycle (2.0 pts):** A program to determine the existence of and, if one exists, display an Eulerian cycle in the graph.

* **4. Bellman-Ford or Dijkstra's Algorithm (2.0 pts):** Implementation of a shortest path algorithm to find the path and distance from the initial vertex to all other vertices in the graph.

* **5. Floyd-Warshall Algorithm (2.0 pts):** A program that calculates the shortest distances between all pairs of vertices in the graph.

* **6. Report (2.0 pts):** Elaboration of a report in PDF format, justifying the data structures selected for each exercise.

The following features were developed for **Activity A2 (EX2)**:

* **1. Strongly Connected Components (2.0 pts):** Implementation of Kosaraju's algorithm to find strongly connected components in directed graphs.

* **2. Topological Sorting (2.0 pts):** Implementation of a depth-first search (DFS) based algorithm for topological sorting of directed acyclic graphs (DAGs).

* **3. Minimum Spanning Tree (2.0 pts):** Implementation of Kruskal's algorithm to find the minimum spanning tree in undirected weighted graphs.

* **4. Report (2.0 pts):** Elaboration of a report in PDF format, justifying the data structures selected for each exercise.

## Team

* Arthur Gislon Leonida
* Matheus Barbieri Munzi

## Repository Structure

```GRAFOS/
├── EX1/
│   ├── pycache/
│   ├── A1_2.py
│   ├── A1_3.py
│   ├── A1_4.py
│   ├── A1_5.py
│   └── graph_utils.py
│   └── .net files for testing
├── EX2/
│   ├── pycache/
│   ├── A2_1.py
│   ├── A2_2.py
│   ├── A2_3.py
│   └── graph_utils.py
│   └── .net files for testing
├── README.md