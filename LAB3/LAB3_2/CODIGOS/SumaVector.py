#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2022 Nestor y Andres.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#


import numpy
import math
from gnuradio import gr

class SumaVector(gr.sync_block):
    """
    docstring for block SumaVector
    """
    def __init__(self, Param1):
        self.Param1 = Param1
        gr.sync_block.__init__(self,
            name="SumaVector",
            in_sig=[(numpy.float32, int(self.Param1))],
            out_sig=[numpy.float32, ])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        for i in range(len(in0)):
            out[i] = math.fsum(in0[i,:])
        return len(output_items[0])
