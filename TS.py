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
        positive = [2]
        negative = [4,5,6]
        goal = 7
        # learning parameter
        gamma = 0.8        
        # how many points in graph? x points
        MATRIX_SIZE = 8
        initial_state = 1
        
        plt.subplot(2, 1, 1)        
        plt.title('Map and path accuracy')
        G=nx.Graph()
        G.add_edges_from(points_list)
        mapping={0:'Start', 1:'1', 2:'2 - Positive', 3:'3', 4:'4 - Negative', 5:'5 - Negative', 6:'6 - Negative', 7:'7 - Goal'} 
        H=nx.relabel_nodes(G,mapping) 
        pos = nx.spring_layout(H)
        nx.draw_networkx_nodes(H,pos, node_size=[200,200,200,200,200,200,200,200])
        nx.draw_networkx_edges(H,pos)
        nx.draw_networkx_labels(H,pos)
        
        # create matrix x*y
        R = np.matrix(np.ones(shape=(MATRIX_SIZE, MATRIX_SIZE)))
        R *= -1
        
        # assign zeros to paths and 100 to goal-reaching point
        for point in points_list:
            print(point)
            if point[1] == goal:
                R[point] = 100
            else:
                R[point] = 0
        
            if point[0] == goal:
                R[point[::-1]] = 100
            else:
                # reverse of point
                R[point[::-1]]= 0
        
        # add goal point round trip
        R[goal,goal]= 100
        
        # re-initialize the matrices for new run
        Q = np.matrix(np.zeros([MATRIX_SIZE,MATRIX_SIZE]))
        
        enviro_positive = np.matrix(np.zeros([MATRIX_SIZE,MATRIX_SIZE]))
        enviro_negative = np.matrix(np.zeros([MATRIX_SIZE,MATRIX_SIZE]))
         

        
        assert(initial_state != goal)
        def available_actions(state):
            current_state_row = R[state,]
            av_act = np.where(current_state_row >= 0)[1]
            return av_act
         
        def sample_next_action(available_actions_range):
            next_action = int(np.random.choice(available_act,1))
            return next_action
        
        def collect_environmental_data(action):
            found = []
            if action in positive:
                found.append('p')
        
            if action in negative:
                found.append('n')
            return (found)
         
        available_act = available_actions(initial_state) 
         
        action = sample_next_action(available_act)
        
        def update(current_state, action, gamma):
          max_index = np.where(Q[action,] == np.max(Q[action,]))[1]
          
          if max_index.shape[0] > 1:
              max_index = int(np.random.choice(max_index, size = 1))
          else:
              max_index = int(max_index)
          max_value = Q[action, max_index]
          
          Q[current_state, action] = R[current_state, action] + gamma * max_value
          #print('max_value', R[current_state, action] + gamma * max_value)
          
          environment = collect_environmental_data(action)
          if 'p' in environment: 
            enviro_positive[current_state, action] += 1
          
          if 'n' in environment: 
            enviro_negative[current_state, action] += 1
          
          if (np.max(Q) > 0):
            return(np.sum(Q/np.max(Q)*100))
          else:
            return (0)
        
        update(initial_state,action,gamma)
        
        scores = []
        for i in range(700):
            current_state = np.random.randint(0, int(Q.shape[0]))
            available_act = available_actions(current_state)
            action = sample_next_action(available_act)
            score = update(current_state,action,gamma)
        
        # environmental matrices
        Q = np.matrix(np.zeros([MATRIX_SIZE,MATRIX_SIZE]))
        
        # subtract bees with smoke, this gives smoke a negative effect
        enviro_matrix = enviro_positive - enviro_negative
        
        # Get available actions in the current state
        available_act = available_actions(initial_state) 
        
        # Sample next action to be performed
        action = sample_next_action(available_act)
        
        # This function updates the Q matrix according to the path selected and the Q 
        # learning algorithm
        def update(current_state, action, gamma):
            
            max_index = np.where(Q[action,] == np.max(Q[action,]))[1]
        
            if max_index.shape[0] > 1:
                max_index = int(np.random.choice(max_index, size = 1))
            else:
                max_index = int(max_index)
            max_value = Q[action, max_index]
        
            Q[current_state, action] = R[current_state, action] + gamma * max_value
        
            environment = collect_environmental_data(action)
            if 'b' in environment: 
                enviro_matrix[current_state, action] += 1
            if 's' in environment: 
                enviro_matrix[current_state, action] -= 1
        
            return(np.sum(Q/np.max(Q)*100))
        
        update(initial_state,action,gamma)
        
        enviro_matrix_snap = enviro_matrix.copy()
        
        def available_actions_with_enviro_help(state):
            current_state_row = R[state,]
            av_act = np.where(current_state_row >= 0)[1]
            # if there are multiple routes, dis-favor anything negative
            env_pos_row = enviro_matrix_snap[state,av_act]
            if (np.sum(env_pos_row < 0)):
                # can we remove the negative directions from av_act?
                temp_av_act = av_act[np.array(env_pos_row)[0]>=0]
                if len(temp_av_act) > 0:
                    av_act = temp_av_act
            return av_act
        
        # Training
        plt.subplot(2, 1, 2)
        scores = []
        for i in range(700):
            current_state = np.random.randint(0, int(Q.shape[0]))
            available_act = available_actions_with_enviro_help(current_state)
            action = sample_next_action(available_act)
            score = update(current_state,action,gamma)
            scores.append(score)
            
        plt.plot(scores)
        plt.show()
    