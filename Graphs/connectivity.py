#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 17:26:46 2018

@author: kristianeschenburg
"""

import traversal
import numpy as np

def is_connected(graph):
    
    """
    Determine if graph is connected.
    
    Parameters:
    - - - - -
        graph : adjacency matrix of graph.
    """
    
    [parents,visited] = traversal.bfs(graph)
    
    return np.any(visited < 1)
    
def connected_components(graph):
    
    """
    Find the connected components of a graph.  Each node will be assigned a 
    value, indicating the component that it belongs to.
    
    Parameters:
    - - - - -
        graph : adjacency matrix of graph
        
    While there is a vertex that is not assigned to a component, run bread 
    first search, starting from one of the unassigned vertices.  For each 
    traversal, assign all visited vertices to the same component.
    """
    
    try:
        [x,y] = graph.shape
    except:
        raise ValueError
    
    nodes = graph.shape[0]
    components = -1*np.ones((nodes,))
    
    c = 0
    while np.any(components == -1):

        source = np.where(components == -1)[0][0]

        [parents,visited] = traversal.bfs(graph,source=source)
        components[np.where(visited)] = c
        
        c += 1

    return [c,components]