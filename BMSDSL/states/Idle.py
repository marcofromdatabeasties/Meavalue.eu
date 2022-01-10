#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 Idle is the start of all the states.

    Copyright (C) Mon Jan 10 11:34:38 2022  @author: ubuntu

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

class Idle(State):
    
    profession = None
      
    def __init__(self, profession):
        self.name = "Idle"
        self.profession = profession
    def transition(self):
        if (self.profession):
            return True, self.profession
        else:
            return False, RunError("No profession defined")
    