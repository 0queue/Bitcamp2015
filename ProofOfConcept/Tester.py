#!/usr/bin/python

from Slicer import Slicer
from metamind.api import ClassificationData, ClassificationModel, set_api_key
import cv2
import sys

if len(sys.argv) < 3:
    print ("Usage: Tester.py <key file> <picture>")
    exit(1)

with open(sys.argv[1], "r") as apikey:
    key = apikey.read()

key = key.rstrip()

set_api_key(key)
classifier = ClassificationModel(id=25011)
print ("-----")

s = Slicer(sys.argv[2], "out.jpg", True)
s.create_slices(150)

i = 0
for slic in s.slics:
    cv2.imwrite("CURRENT" + str(i) + ".jpg", slic)
    print classifier.predict(["CURRENT" + str(i) + ".jpg"], input_type="files")
    i += 1
