# -*- coding: utf-8 -*-
"""
Travelling Salesman Graphs

@author: Amber
"""

#imports
import numpy as np
import pylab as plt
import networkx as nx


def TS1Graph():
        # map cell to cell, add circular cell to goal point: make context appropriate
        points_list = [(0,1), (1,5), (5,6), (5,4), (1,2), (2,3), (2,7)]
        bees = [2]
        smoke = [4,5,6]
        goal = 7
        # learning parameter
        gamma = 0.8
        
        G=nx.Graph()
        G.add_edges_from(points_list)
        mapping={0:'Start', 1:'1', 2:'2 - Bees', 3:'3', 4:'4 - Smoke', 5:'5 - Smoke', 6:'6 - Smoke', 7:'7 - Beehive'} 
        H=nx.relabel_nodes(G,mapping) 
        pos = nx.spring_layout(H)
        nx.draw_networkx_nodes(H,pos, node_size=[200,200,200,200,200,200,200,200])
        nx.draw_networkx_edges(H,pos)
        nx.draw_networkx_labels(H,pos)
        #plt.figure(figsize=(20,14))
        plt.show()

