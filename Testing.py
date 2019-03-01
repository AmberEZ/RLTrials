# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:51:33 2019
File to contain unit testing code
This file will test the functions in "RLGUI.py" and "TS.py". But only those that have a recordable output.

@author: Amber
"""

import unittest
import numpy as np
import numpy.testing as npt
import RLGUI
import TS


#class TestRLGUI(unittest.TestCase):
"""
functions in RLGUI:
    RLTrialsGUI_tk class:
        __init__
        initialize
        OnTSButtonClick
None of them have outputs
"""

            
class TestTS(unittest.TestCase):
        """
        functions in TS:
            TS1Graph(goal, initial_state, MATRIX_SIZE, gamma) - no return values
                available_actions(self) - takes an integer (state), returns an integer (row)
                sample_next_action(available_actions_range) - takes an integer (row), returns an integer (action)
                collect_environmental_data(action) - takes an integer(action), returns a list (found)
                update(current_state, action, gamma) - takes an integer (state), another integer (action) and a decimal number (gamma, the learning parameter)
                available_actions_with_enviro_help(state) - takes an integer (state) and returns an integer (row)
            
        """
        def test_available_actions(self): #takes an integer (state) and matrix(R), returns an array
            npt.assert_array_equal(TS.available_actions(1, np.matrix([[1, 2], [3, 4]]) ), [0, 1] )
            
#        def test_sample_next_action(available_actions_range):
#            
#        def test_collect_environmental_data(action):
#            
#        def test_update(current_state, action, gamma):
#            
#        def test_available_actions_with_enviro_help(state):


if __name__ == '__main__':
    unittest.main()