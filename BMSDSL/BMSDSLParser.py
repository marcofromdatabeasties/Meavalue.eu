                                                #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 Loads a BMS from a file that contains it. This file is executable. Using  Takagi-Sugeno Rules for now.
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
    
    def __init__(self, currentProfession = None ):    
        self.tags = ["Profession", "Behaviour", "Marker", "Source", "APA", "Rule", "QualityAttribute" ]
        self.currentProfession = currentProfession
        self.currentBehaviour = None
        self.currentMarker = None
        self.currentQualityAttribute = None
        self.currentRule = None
        self.variables = []
        self.results = []
    
    def loadFile(self, name):
        text_file = open(name, "r")
        return text_file.read()
    
    def parseString(self, raw):    
        content = self.splitStringInStates(raw)
        for idx, state in enumerate(content):
            remarks = []
            if (state in self.tags):
                allResult = False
                
                result, txt = self._snifAndProcessProfession(state, content, idx)
                allResult = allResult or result
                if (result):
                    remarks.append(txt)
                
                self._snifAndProcessBehaviour( state, content, idx)
                allResult = allResult or result
                if (result):
                    remarks.append(txt)

                self._snifAndProcessMarker(state, content, idx)
                allResult = allResult or result
                if (result):
                    remarks.append(txt)

                self._snifAndProcessQA(state, content, idx)
                allResult = allResult or result
                if (result):
                    remarks.append(txt)

                self._snifAndProcessRule(state, content, idx)
                allResult = allResult or result
                if (result):
                    remarks.append(txt)
                    
                
        return allResult, remarks
                
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
                if (self.currentProfession.hasBehaviour(content[idx + 1])):
                    self.currentBehaviour = self.currentProfession.getBehaviour(content[idx + 1])
                else:
                    self.currentBehaviour = Behaviour(content[idx + 1])
                    self.currentProfession.addBehaviour(self.currentBehaviour)
                return False, ""                                       
    
    def _snifAndProcessMarker(self, state, content, idx):
        if state == "Marker":
            if (self.currentProfession == None or self.currentBehaviour == None):
                return True, format("Marker %s defined but no profession and behaviour declared first.", content[idx + 1])
            else:
                if (self.currentBehaviour.hasMarker(content[idx + 1])):
                    self.currentMarker = self.currentBehaviour.getMarker(content[idx + 1])
                else:
                    self.currentMarker = Marker(content[idx + 1])
                    self.currentBehaviour.addMarker(self.currentMarker)
                return False, "" 
                
    def _snifAndProcessQA(self, state, content, idx):
        if state == "QualityAttribute":
            if (self.currentProfession == None or self.currentBehaviour == None or self.currentMarker == None):
                return True, format("QualityAttribute %s defined but no profession, behaviour, and marker declared first.", content[idx + 1])
            else:
                if (self.currentMarker.hasQualityAttribute(content[idx + 1])):
                    self.currentQualityAttribute = self.currentMarker.getQualityAttribute(content[idx + 1])
                else:
                    self.currentQualityAttribute = QualityAttribute(content[idx + 1])
                    self.currentMarker.addQualityAttribute(self.currentQualityAttribute)
                return False, "" 
        
    def _snifAndProcessRule(self, state, content, idx):
        if (self.currentProfession == None or self.currentBehaviour == None or self.currentMarker == None or self.currentQualityAttribute == None):
                return True, "Rule {} defined but no profession, behaviour, marker, or Quality Attribute declared first.".format( content[idx + 1])
        else:
            self.currentRule = Rule(content[idx + 1])
            self.currentQualityAttribute.QARule(self.currentRule)
            error, txt = self._extractVariables(self.currentRule)
            if not error:
                return self._ruleConsistentWithQA(self.currentQualityAttribute, self.currentRule)
            else:
                return error, txt;
            
    def parsefile(self, name):
        raw = self.loadFile(name)
        
        return self.variables, self.parseString(raw)
    
    def _extractVariables(self, rule):
        ruleParts = re.split(r"THEN", rule.rule)
        if (len(ruleParts) == 2):
            inp = ruleParts[0]
            outp = ruleParts[1]
            
            defines = re.findall(r"(\w+ IS \w+)", inp)
            for defn in defines:
                names = re.split(r" IS .*", defn)
                for name in names:
                    if len(name) and name not in self.variables:
                        self.variables.append(name)
            if not len(self.variables):
                return True, "If should contain inputs (either QA or Measurements)"
            
            defines = re.findall(r"(\w+ IS \w+)", outp)
            if len(defines)>1:
                return True, "More than one assignment to QA is not allowed."
            else:
                names = re.split(r" IS .*", defines[0])
                self.results.append(names[0]);
                return False, ""                        
        else:
            return True, "Rule should contain one THEN"
        
    #needs extract variables to run first    
    def _ruleConsistentWithQA(self, QA, Rule):
        if QA.giveName() not in self.results:
            return True, "Rule should contain the result {} of a QA".format( QA.giveName())
        else:
            return False, ""            


if __name__ == '__main__':
    parser = BMSDSLParser(sys.argv[1])
    