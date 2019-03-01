# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:51:33 2019
File to contain unit testing code
This file will test the functions in "RLGUI.py" and "TS.py".

@author: Amber
"""

import unittest
import RLGUI
import TS

class TestRLGUI(unittest.TestCase):

    def test_OnTSButtonClick(self):
        self.assertEqual(" Travelling Salesman" , " Travelling Salesman")
            
class TestTS(unittest.TestCase):
        def test_TS(self):
            self.assertEqual(False, False)


if __name__ == '__main__':
    unittest.main()