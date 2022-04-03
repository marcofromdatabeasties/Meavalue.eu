                                                #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 Loads a BMS from a file that contains it. This file is executable.
 BMS example:
     Profession: "Programmer"
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
                         ....
                     QualityAttribute: "Number of lines in Class"
                         
                         ....
                    QualityAttribute: ""
                    .....

    Copyright (C) Thu Feb 17 14:03:56 2022  @author: Marco Dumont

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
import re
import sys
import BMSDSL.states

from BMSDSL.states.Profession import Profession
from .states.Behaviours import Behaviour
from .states.Markers import Marker
from .states.Quality import QualityAttribute
from .states.Rules import Rule

class BMSDSLParser:
    tags = ["Profession", "Behaviour", "Marker", "Source", "APA", "Rule", "QualityAttribute" ]
    currentProfession = None
    currentBehaviour = None
    currentMarker = None
    currentQualityAttribute = None
    currentRule = None
    
    def loadFile(self, name):
        text_file = open(name, "r")
        return text_file.read()
    
    def parseString(self, raw):    
        content = self.splitStringInStates(raw)
        for idx, state in enumerate(content):
            if (state in self.tags):                                                   
                self._snifAndProcessProfession(state, content, idx)
                self._snifAndProcessBehaviour( state, content, idx)
                self._snifAndProcessMarker(state, content, idx)
                self._snifAndProcessQA(state, content, idx)
                self._snifAndProcessRule(state, content, idx)
                
    def splitStringInStates(self, raw):
        result = re.split(":|\n", raw)
        for idx,info in enumerate(result):
            result[idx] = info.strip()
        return result
    
                
    def _snifAndProcessProfession(self, state, content, idx):
        if state == "Profession":
            self.currentProfession = Profession(content[idx + 1]);
            self.currentBehaviour = None
            self.currentMarker == None
            self.currentQualityAttribute = None
            self.currentRule = None
        return False
    
    def _snifAndProcessBehaviour(self, state, content, idx):
        if state == "Behaviour":
            if (self.currentProfession == None):
                return True, format("Behaviour %s defined but no profession declared first.", content[idx + 1])
            else:
                self.currentMarker == None
                self.currentBehaviour = Behaviour(content[idx + 1])
                self.currentProfession.addBehaviour(self.currentBehaviour)
                return False, ""                                       
    
    def _snifAndProcessMarker(self, state, content, idx):
        if state == "Marker":
            if (self.currentProfession == None or self.currentBehaviour == None):
                return True, format("Marker %s defined but no profession and behaviour declared first.", content[idx + 1])
            else:
                self.currentMarker = Marker(content[idx + 1])
                self.currentBehaviour.addMarker(self.currentMarker)
                return False, "" 
                
    def _snifAndProcessQA(self, state, content, idx):
        if state == "QualityAttribute":
            if (self.currentProfession == None or self.currentBehaviour == None or self.currentMarker == None):
                return True, format("QualityAttribute %s defined but no profession, behaviour, and marker declared first.", content[idx + 1])
            else:
                self.currentQualityAttribute = QualityAttribute(content[idx + 1])
                self.currentMarker.addQualityAttribute(self.currentQualityAttribute)
                return False, "" 
        
    def _snifAndProcessRule(self, state, content, idx):
        if (self.currentProfession == None or self.currentBehaviour == None or self.currentMarker == None or self.currentQualityAttribute == None):
                return True, format("Rule %s defined but no profession, behaviour, marker, or Quality Attribute declared first.", content[idx + 1])
        else:
            self.currentRule = Rule(content[idx + 1])
            self.currentQualityAttribute.addRule(self.currentRule)
            return False, ""
            
    def parsefile(self, name):
        raw = self.loadFile(name)
        self.parseString(raw)
        


if __name__ == '__main__':
    parser = BMSDSLParser(sys.argv[1])
    