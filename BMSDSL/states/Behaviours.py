#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 This class captures the the behaviours
 At least one or more behaviours. The makeup of a Behaviour event is: Behaviour: "<name>" 
         
         Profession: "Programmer"
             Behaviour: "Write code of good quality"
                 Source: 
                     APA: "{APA reference}"
                 Marker:  "Create code of quality"
                     QualityAttribute: "Coupling"
                         Source: 
                             APA: "{APA reference}"
                         Rule: "IF (Intense_Coupling IS high) and (External_Coupling IS high) THEN (Coupling IS high)"
                            Source: 
                                 APA: "{APA reference}"
                         ....
                     QualityAttribute: "Number of lines in Class"
                         
                         ....
                    QualityAttribute: ""
                    .....

    Copyright (C) Mon Jan 10 20:35:16 2022  @author: ubuntu

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

from BMSDSL.states.State import State
from BMSDSL.states.RunErrorState import DSLRunError
 

class Behaviour(State):
    
    def __init__(self, name):
        self.name = name
        self.markers = {}
        self.tag = "Behaviour:"
    #transition() return the markers associated with this profession in the
    #DSl. At least one marker should be present. When none is supplied while
    #processing a error is returned.
    def transition(self):
        if (len(self.markers)):
            return False, self.markers
        else:
            return True, DSLRunError("No markers defined")
        
    def addMarker(self, marker):
        self.markers[marker.giveName()] = marker
        
    def hasMarker(self, markerName):
        return markerName in self.markers
        
    def getMarker(self, markerName):
        return self.markers[markerName]
