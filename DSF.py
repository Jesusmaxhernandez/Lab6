#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Jesus Maximino Hernandez
CS 2302 Data Structures - Diego Aguirre
TA - Manoj Saha
Lab 6 - Option A 

@author: JesusMHernandez
"""

class DisjointSetForest:
    def __init__(self, n):
        self.dsf = [-1] * n

    def is_index_valid(self, index):
        return 0 <= index <= len(self.dsf)

    def find(self, a):  # <--- find with path compression
        if not self.is_index_valid(a):
            return -1

        if self.dsf[a] < 0:
            return a

        #self.dsf[a] = self.find(self.dsf[a])
        return self.dsf[a]

    def union(self, a, b):  # <--- union by height
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:  # Don't do anything if they belong to the same set already
            return

        if self.dsf[ra] == self.dsf[rb]:  # Trees have the same height
            self.dsf[ra] -= 1
            self.dsf[rb] = ra
        elif self.dsf[ra] < self.dsf[rb]:
            self.dsf[rb] = ra
        else:
            self.dsf[ra] = rb
            
    def is_element_singleton(self, i):
        if not self.is_index_valid(i):
            return False

        if self.dsf[i] >= 0:
            return False

        for num in self.dsf:
            if num == i:
                return False

        return True
    
    def are_all_paths_compressed(self):  # <--- (problem 2 answer) O(n)
        for i in range(len(self.dsf)):
            if self.dsf[i] >= 0 and self.dsf[self.dsf[i]] >= 0:
                return False

        return True
    
    def create_dsf(n, k):
        dsf = [-1] * (n * k)

        for i in range(len(dsf)):
            if i % k != 0:
                dsf[i] = i - 1

        return dsf
