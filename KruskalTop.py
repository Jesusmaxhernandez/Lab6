#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Jesus Maximino Hernandez
CS 2302 Data Structures - Diego Aguirre
TA - Manoj Saha
Lab 6 - Option A 

@author: JesusMHernandez
"""

#from GraphAL import GraphAL
from GraphAM import GraphAM
from collections import deque
from DSF import DisjointSetForest


def kruskals_alg(gr):
    """
    Implements Kruskals Algorithm on a graph
    """
    
    if gr.adj_list is None:
        return None
    T = list()
    for i in range (len(gr.adj_list)):
        temp = gr.adj_list[i]
        while temp != None:
            T.append([i, temp.item, temp.weight])
            temp = temp.next
     
def kruskals(graph):
    
    
    sorted_edges = list()
    sorted_edges = sort_edges(graph)
    T = []
    
    #tree = DisjointSetForest(len(graph.adj_matrix))
    #DSF to check for cycles
    dsf = DisjointSetForest(len(graph.adj_matrix))

    for src in range(len(graph.adj_matrix)):
        for dest in range(len(graph.adj_matrix)):
            if graph.adj_matrix[src][dest] != 0:
                if dsf.find(src) == dsf.find(dest):
                    break
                else:
                    dsf.union(src, dest)
                    T.append(graph.adj_matrix[src][dest])
    return T
def sort_edges(graph):
    
    sorted_edges_list = list()
    seen_list = list()
    
    for i in range(len(graph.adj_matrix)):
        for j in range(len(graph.adj_matrix)):
            if graph.adj_matrix[i][j] not in seen_list:
                if graph.adj_matrix[i][j] != 0:
                     sorted_edges_list.append(graph.adj_matrix[i][j])
                     seen_list.append(graph.adj_matrix[j][i])
                     
    sorted_edges_list.sort() #edges are sorted 
    
    return sorted_edges_list
    
def topological_sort(graph):
  """
  Implements topological sort algorithm on a graph object.
  
  Args:
    graph: A GraphAL object
  
  Returns:
    sort_result: A topological sortng of the vertices in the graph as a
                 list
  """
  if graph.adj_list is None:
    return None
  all_in_degrees = compute_indegree(graph)
  sort_result = list()
  
  # Python deque used here as queue
  queue = deque([])
  
  for i in range(len(all_in_degrees)):
    if all_in_degrees[i] == 0:
      queue.append(i)
  
  
  while len(queue) != 0:
    u = queue.popleft()
    sort_result.append(u)
    
    for adj_vertex in graph.get_adj_vertices(u):
      all_in_degrees[adj_vertex] -= 1
      
      if all_in_degrees[adj_vertex] == 0:
        queue.append(adj_vertex)
  # Returns None if a cycle is detected
  if len(sort_result) != len(graph.adj_list):
    return None
  
  return sort_result

def compute_indegree(graph):
    """
    Function to get indegress for every vertoc 
    """
    if graph.adj_list is None:
        return None
    final = [0] * len(graph.adj_list)
    for i in range(len(graph.adj_list)):
        temp = graph.adj_list[i]
        while temp != None:
            final[temp.item] += 1
            temp = temp.next
            
    return final
