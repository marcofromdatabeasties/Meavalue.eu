#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 Base class for the states of the DSL states help in parsing the .bms files.

    Copyright (C) Mon Jan 10 11:13:35 2022  @author: Marco Dumont

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

class State:
    
    def __init__(self):
        self.name = ""
        self.tag = ""
        self.sources = []
    
    def transition(self):
        print ("This should not be shown")
        #no code yet
    def isState(self, tag):
        return self.tag == self.tag
    
    def giveName(self):
        return self.name
    
    def addSource(self, apa):
        self.sources.append(apa)