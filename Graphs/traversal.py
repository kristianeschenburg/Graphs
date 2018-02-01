#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 17:20:04 2018

@author: kristianeschenburg
"""

from Queue import Queue
import numpy as np

def bfs(graph,s,t):
    
    """
    Breadth first search from source vertex s to target vertex t.  Returns the
    final path.  If there is no path, list will be empty.
    
    Parameters:
    - - - - -
        graph : directed adjacency matrix, where rows are source nodes of
                an edge, and columns are target nodes of an edge
        s : source node from which to search for a path
        t : target node to which to search for path
    """
    
    visited = np.zeros((graph.shape[0],)).astype(np.int32)
    parent = np.zeros((graph.shape[0],)).astype(np.int32)
    parent[s] = -1
    
    Q = Queue()
    Q.put(s)

    bfs_path = []

    while not Q.empty():
        
        vertex = Q.get()

        for n in np.arange(graph.shape[1]):
            if not visited[n] and graph[vertex][n]:
                
                parent[n] = vertex
                
                if n == t:

                    return path(parent,t)
                
                Q.put(n)

        visited[vertex] = 1
    
    return bfs_path

def path(parents,t):
    
    """
    Build path from source to target.
    """
    
    rev_path = []
    rev_path.append(t)
    
    while parents[t] != -1:
        rev_path.append(parents[t])
        t = parents[t]

    path = []
    while len(rev_path) != 0:
        path.append(rev_path.pop())
        
    return path