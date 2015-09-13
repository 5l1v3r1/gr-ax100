#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2015 <+YOU OR YOUR COMPANY+>.
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
from gnuradio import gr
from bitarray import bitarray

class descrambler(gr.sync_block):
    """
    docstring for block descrambler
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="descrambler",
            in_sig=[<+numpy.float+>],
            out_sig=[<+numpy.float+>])

        sr = bitarray()
        for i in range(18):
            sr.append(0)

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        for i in range(len(in0):
            out[i] = sr[0] ^ sr[12] ^ sr[17]
            sr.insert(0, in0[i] & 0x01)
            sr.pop()

        return len(output_items[0])
