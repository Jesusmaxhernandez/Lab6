#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 20:47:55 2018

@author: JesusMHernandez
"""

from GraphAL import GraphAL
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
            
def sort_key(elem):
    """
    Function to sort weights

    """
    return elem[2]

    edges = sorted(edges, key=sort_key)
    tree = list()
    
    dsf = DisjointSetForest(len(gr.adj_list))
    for edge in edges:
        if dsf.find(edge[0]) != dsf.find(edge[1]):
          dsf.union(edge[0], edge[1])
          tree.append(edge)
    
    return tree

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