#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 This class holds the Profession state. The root of the DSL this initiates the BMS and acts as a stating point.
 
 Example:
     In the .bms file the following structure is expected:
         At least one Profession. The makeup of a Profession event is: Profession: "<name>" 
         
         Profession: "Programmer"
             Behaviour: "Write code of good quality"
                 Source: 
                     APA: "{APA reference}"
                 Marker:  "Create code of quality"
                     QualityAttribute: "Coupling"
                         Source: 
                             APA: "{APA reference}"
                         Measurement: "Intense Coupling" ^ "External Coupling"
                             Source: 
                                 APA: "{APA reference}"
                         ....
                     QualityAttribute: "Number of lines in Class"
                         Measurement: "Lines in Class"
                         ....
                    QualityAttribute: ""
                    .....
                
    Copyright (C) Mon Jan 10 10:53:55 2022  @author: Marco Dumont

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
import State.State as State
import RunErrorState.RunError as RunError
 

class Profession(State):
    behaviours = {}
    
    def __init__(self, name, behaviours):
        self.name = name
        self.behaviours = behaviours
        self.tag = "Profession:"
    
    def transition(self):
        if (len(self.behaviours)):
            return True, self.behaviours
        else:
            return False, RunError("No behaviours defined")
        