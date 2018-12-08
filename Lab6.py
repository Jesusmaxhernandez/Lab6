#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jesus Maximino Hernandez
CS 2302 Data Structures - Diego Aguirre
TA - Manoj Saha
Lab 6 - Option A 

@author: JesusMHernandez
"""

from KruskalTop import topological_sort
from KruskalTop import kruskals
from KruskalTop import sort_edges
from GraphAM import GraphAM


def main():

  print("[source, dest, weight]")
  print()
  # Kruskal Graph 1
  # 0-6-2
  # |  /|
  # 1 5 4
  # |/  |
  # 1-3- 3
  graph_kruskals = GraphAM(initial_num_vertices=4, is_directed=False)

  graph_kruskals.add_edge(0, 2, 6)
  graph_kruskals.add_edge(2, 3, 4)
  graph_kruskals.add_edge(0, 1, 1)
  graph_kruskals.add_edge(2, 1, 5)
  graph_kruskals.add_edge(1, 3, 3)
  
  print("Graph 1 kruskals:")
  print(kruskals(graph_kruskals))

  # Kruskal Graph 2
  graph_kruskals = None
  graph_kruskals = GraphAM(initial_num_vertices=5, is_directed=False)

  graph_kruskals.add_edge(0, 1, 6)
  graph_kruskals.add_edge(1, 3, 4)
  graph_kruskals.add_edge(0, 2, 1)
  graph_kruskals.add_edge(1, 2, 5)
  graph_kruskals.add_edge(1, 4, 2)
  graph_kruskals.add_edge(3, 4, 3)

  print("Graph 2 kruskals:")
  print(kruskals(graph_kruskals))
  

  print()
#   /--> 1 -> 4 -> 7 -\
#  /                   \
# 0 -> 2 -> 5 -> 8------> 10
#  \                  /
#  \--> 3 -> 6 -> 9--/

  print("Graph 1 topological order:")
  graph_top = GraphAL(initial_num_vertices=11, is_directed=True)

  graph_top.add_edge(0, 1)
  graph_top.add_edge(0, 2)
  graph_top.add_edge(0, 3)

  graph_top.add_edge(1, 4)
  graph_top.add_edge(2, 5)
  graph_top.add_edge(3, 6)

  graph_top.add_edge(4, 7)
  graph_top.add_edge(5, 8)
  graph_top.add_edge(6, 9)
  
  graph_top.add_edge(7, 10)
  graph_top.add_edge(8, 10)
  graph_top.add_edge(9, 10)

  print(topological_sort(graph_top))
  

  print("Graph 2 topological order:")
  graph_topological = None
  graph_topological = GraphAL(initial_num_vertices=4, is_directed=True)
  graph_topological.add_edge(0, 3)
  graph_topological.add_edge(3, 2)
  graph_topological.add_edge(0, 1)
  graph_topological.add_edge(1, 2)

  print(topological_sort(graph_topological))

main()
