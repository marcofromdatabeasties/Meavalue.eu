#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 A marker describes observable behaviour and is therefore a subset of behaviours.

    Copyright (C) Wed Jan 12 15:38:17 2022  @author: ubuntu

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

class Marker (State):
    
    def __init__(self, name):
        self.name = name
        self.qualityAttributes = {}
        self.tag = "Marker:"
      
    #transition() return the QA's associated with this profession in the
    #DSl. At least one QA should be present. When none is supplied while
    #processing a error is returned.    
    def transition(self):
        if (len(self.qualityAttributes)):
            return False, self.qualityAttributes
        else:
            return True, DSLRunError("No markers defined")
        
    def addQualityAttribute(self, qualityAttribute):
        self.qualityAttributes[qualityAttribute.giveName()] = qualityAttribute
        
    def hasQualityAttribute(self, qualityAttributeName):
        return qualityAttributeName in self.qualityAttributes
    
    def getQualityAttribute(self, qualityAttributeName):
        return self.qualityAttributes[qualityAttributeName]