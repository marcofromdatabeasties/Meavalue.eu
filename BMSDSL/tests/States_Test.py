#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 <one line to give the program's name and a brief idea of what it does.>

    Copyright (C) Mon Jan 10 20:51:21 2022  @author: ubuntu

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
import unittest
from BMSDSL.states.Profession import Profession
from BMSDSL.states.Behaviours import Behaviour

class TestNProfession(unittest.TestCase):
    def test_Profession_transition_No_Behaviours(self):
        prof = Profession("Test", {})
        error, dummy = prof.transition()
        
        self.assertEqual(error, True)
    
    def test_Profession_transition_Behaviours(self):
        prof = Profession("Test", {"behav": Behaviour("behav", {}, {})})
        error, dummy = prof.transition()
        
        self.assertEqual(error, False)
    
    
if __name__ == '__main__':
    unittest.main()