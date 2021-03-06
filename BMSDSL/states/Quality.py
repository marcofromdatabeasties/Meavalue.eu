#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 This state holds the QualityAttribute.

    Copyright (C) Wed Jan 12 16:07:51 2022  @author: Marco Dumont

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

class QualityAttribute(State):
    def __init__(self, name):
        self.name = name
        self.rules = []
        self.tag = "QualityAttribute:"
    #transition() return the measurements associated with this profession in the
    #DSl. At least one QualityAttribute should be present. When none is supplied while
    #processing a error is returned.
    def transition(self):
        if len(self.rules):
            return False, self.rules
        else:
            return True, DSLRunError("No measurements defined")
        
    def QARule(self, rule):
        if (rule not in self.rules):
            self.rules.append(rule)