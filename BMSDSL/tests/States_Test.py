#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 The purpose of this file is to test states and transitions

    Copyright (C) Mon Jan 10 20:51:21 2022  @author: Marco Dumont

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
from BMSDSL.states.Markers import Marker
from BMSDSL.states.Quality import QualityAttribute
from BMSDSL.states.Rules import Rule

class TestNProfession(unittest.TestCase):
    def test_Profession_transition_No_Behaviours(self):
        prof = Profession("Test", {}, {})
        error, dummy = prof.transition()
        
        #expected is an error
        self.assertEqual(error, True)
    
    def test_Profession_transition_Behaviours(self):
        prof = Profession("Test", {"behav": Behaviour("behav", {}, {})}, {})
        error, dummy = prof.transition()                                    
        #expected is no error
        self.assertEqual(error, False)
    
class TestBehaviour(unittest.TestCase):
    def test_Behaviour_transition_No_Markers(self):
        beh = Behaviour("Test", {}, {})
        error, dummy = beh.transition()
        #expected is an error
        self.assertEqual(error, True)

    def test_Behaviour_transition_Markers(self):
        beh = Behaviour("Test", {"marker" : Marker("mark", {}, {})}, {})
        error, dummy = beh.transition()
        #expected is no error
        self.assertEqual(error, False)

class TestMarkers(unittest.TestCase):
    def test_Markers_transition_No_QA(self):
        beh = Marker("Marker", {}, {})
        error, dummy = beh.transition()
        #expected is an error
        self.assertEqual(error, True)

    def test_Markers_transition_QA(self):
        beh = Marker("Test", {"Marker" : QualityAttribute("QA", {}, {})}, {})
        error, dummy = beh.transition() 
        #expected is no error
        self.assertEqual(error, False)
        
class TestQualityAttribute(unittest.TestCase):
    def test_QualityAttribute_transition_No_Rule(self):
        beh = QualityAttribute("QA", {}, {})
        error, dummy = beh.transition()
        #expected is an error
        self.assertEqual(error, True)

    def test_QualityAttribute_transition_Rule(self):
        beh = QualityAttribute("Test", {"QA" : Rule("IF Rule THEN Rule_the_world IS high")}, {})
        error, dummy = beh.transition()
        #expected is no error
        self.assertEqual(error, False)


        
if __name__ == '__main__':
    unittest.main()