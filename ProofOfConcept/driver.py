#!/usr/bin/python

from Slicer import Slicer 
import sys

s = Slicer(sys.argv[1], "out.jpg", True)

s.create_slices(150)
s.output_slices("slice")
