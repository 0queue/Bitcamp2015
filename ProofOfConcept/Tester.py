#!/usr/bin/python

from Slicer import Slicer
from metamind.api import ClassificationData, ClassificationModel, set_api_key
import sys

if len(sys.argv) < 2:
    print ("Usage: Tester.py <key file> <picture>")
    exit(1)

with open(sys.argv[1], "r") as apikey:
    key = apikey.read()

key = key.rstrip()

print ("|" + key + "|")
set_api_key(key)
