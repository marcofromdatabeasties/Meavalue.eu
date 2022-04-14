#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 Atoms represent a value (measurement), logical function (predicate), Rule 
 ( f.i. Takagi-Sugeno / Mamdani) or,  and, or and not. As the most
 simple building blocks of a measurement. 

    Copyright (C) Mon Jan 24 12:14:57 2022  @author: Marco Dumont

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
import uuid
from BMSDSL.states.State import State
from BMSDSL.states.RunErrorState import DSLRunError


class Rule(State):
    def __init__(self, rule):
        self.rule = rule
        self.tag = "Rule:"
        self.name = uuid.uuid4()
        
    def transition(self):
        if (len(self.rules)):
            return False, self.rules
        else:
            error = DSLRunError("No behaviours defined")
            return True, error

        