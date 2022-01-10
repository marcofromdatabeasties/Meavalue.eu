#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 The RunError is a state the defines that the program does not fullfill it's
 contract.

    Copyright (C) Mon Jan 10 11:29:08 2022  @author: Marco Dumont

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

class DSLRunError(State):

    message = ""

    def __init__(self, message):        
        self.name = "Conditional error"
        self.message = f"Conditional error {message}"

    def transition(self):
        return True, self
