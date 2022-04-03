#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

  <one line to give the program's name and a brief idea of what it does.>

    Copyright (C) Wed Mar 16 10:38:51 2022  @author: ubuntu

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
import BMSDSL.states
from BMSDSL.BMSDSLParser import BMSDSLParser
from BMSDSL.states.Profession import Profession
from BMSDSL.states.Behaviours import Behaviour
from BMSDSL.states.Markers import Marker
from BMSDSL.states.Quality import QualityAttribute
from BMSDSL.states.Rules import Rule
                   
class TestBMSDSLParser(unittest.TestCase):
    raw = """Profession: "Programmer"
                 Behaviour: "Write code of good quality"
                     Source: 
                         APA: "{APA reference}"
                     Marker:  "Create code of quality"
                         QualityAttribute: "Coupling"
                             Source: 
                                 APA: "{APA reference}"
                             Rule: "IF (Internal_Coupling IS high) and (External_Coupling IS high) THEN (Coupling IS high)"
                                Source: 
                                     APA: "{APA reference}"
        """
    #happy days
    
    def test_SniffingForProfession(self):
        parser = BMSDSLParser()
        testContent = parser.splitStringInStates(self.raw)
        
        print (testContent)
        
        error = parser._snifAndProcessProfession(testContent[0], testContent, 0) 
        self.assertEqual(error, False, "Returns no error")
        self.assertEqual(parser.currentProfession.name , "\"Programmer\"", "Should be programmer")
        
    def test_SniffingForBehaviour(self):
        parser = BMSDSLParser()
        parser.currentProfession = Profession("Test of behaviour")

        testContent = parser.splitStringInStates(self.raw)
        
        error, txt = parser._snifAndProcessBehaviour(testContent[2], testContent, 2) 
        self.assertEqual(error, False, "Returns no error")
        self.assertEqual(parser.currentBehaviour.name , '"Write code of good quality"', "Should be \"Write code of good quality\"")
        
    def test_SnifAndProcessMarker(self):
        parser = BMSDSLParser()
        parser.currentProfession = Profession("Test of behaviour")
        parser.currentBehaviour= Behaviour("Test of behaviour")
        
        testContent = parser.splitStringInStates(self.raw)
        
        error, txt = parser._snifAndProcessMarker(testContent[8], testContent, 8) 
        self.assertEqual(error, False, "Returns no error")
        self.assertEqual(parser.currentMarker.name , '"Create code of quality"', "Should be Create code of quality")
        
    def test_SnifAndProcessQA(self):
        parser = BMSDSLParser()
        parser.currentProfession = Profession("Test of behaviour")
        parser.currentBehaviour = Behaviour("Test of behaviour")
        parser.currentMarker = Marker("Test of marker")
        
        testContent = parser.splitStringInStates(self.raw)
        
        error, txt = parser._snifAndProcessQA(testContent[10], testContent, 10) 
        self.assertEqual(error, False, "Returns no error")
        self.assertEqual(parser.currentQualityAttribute.name , '"Coupling"', "Should be Coupling" )
        
    def test_snifAndProcessRule(self):
        parser = BMSDSLParser()
        parser.currentProfession = Profession("Test of behaviour")
        parser.currentBehaviour = Behaviour("Test of behaviour")
        parser.currentMarker = Marker("Test of marker")
        parser.currentQualityAttribute = QualityAttribute("Test of QA")
        
        testContent = parser.splitStringInStates(self.raw)
        
        error, txt = parser._snifAndProcessRule(testContent[16], testContent, 16) 
        self.assertEqual(error, False, "Returns no error")
        self.assertEqual(parser.currentRule.rule, '"IF (Internal_Coupling IS high) and (External_Coupling IS high) THEN (Coupling IS high)"', "Should be IF (Internal_Coupling IS high) and (External_Coupling IS high) THEN (Coupling IS high)" )
        self.assertEqual(parser.currentQualityAttribute.rule.rule, '"IF (Internal_Coupling IS high) and (External_Coupling IS high) THEN (Coupling IS high)"', "Should be IF (Internal_Coupling IS high) and (External_Coupling IS high) THEN (Coupling IS high)" )
        
if __name__ == '__main__':
    unittest.main()
    
    