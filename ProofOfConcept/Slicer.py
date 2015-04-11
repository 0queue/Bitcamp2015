#!/bin/bash

# A class to slice a picture into shelves

import cv2
import numpy as np
import sys
import copy

class Slicer:

    DEBUG = True

    def __consolidate (self, arr, dv):
        '''Takes an array and difference value (dv), and runs over the array, averaging adjacent
           values if they are within the dv. Modifies arr in place'''
        for i in range (len(arr) - 1):
            if arr[i+1] - arr[i] < dv:
                arr[i] = (arr[i] + arr[i+1])/2
                arr[i+1] = arr[i]

    def __uniq (self, arr):
        '''essentially does sort | uniq on an array. Returns the new array'''
        l = list(set(arr))
        l.sort()
        return l

    def __output_dbg_img (self):
        dbgimg = copy.deepcopy(self.img)
        for y in self.ys:
            cv2.line(dbgimg, (0, y), (dbgimg.shape[1], y), (0, 255, 0))
        cv2.imwrite(self.dbg_path, dbgimg)
            

    def __init__(self, img_path, dbg_path, dbg):
        '''takes a path to an image, a path to the debug image output, and whether or not to debug.
           it then automatically gets the y vals of the shelves'''
        self.img = cv2.imread(img_path)
        self.dbg_path = dbg_path
        self.DEBUG = dbg
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        ret,bw = cv2.threshold(gray, 200,230, cv2.THRESH_BINARY)
        edges = cv2.Canny(bw, 100, 200, apertureSize=3)

        # input, rho, theta, threshold
        # basically where all tuning can happen
        lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=7)

        self.ys = []
        variance = 10
        for x0,y0,x1,y1 in lines[0]:
            if y0-y1 < variance and y0-y1 > -variance:
                self.ys.append(y0)

        self.ys.sort()

        if self.DEBUG:
            print self.ys

        for i in range(0, 100):
            self.__consolidate(self.ys, 50)

        print self.ys

        self.ys = self.__uniq(self.ys)
        self.ys.insert(0, 0) # zero is the first y value

        if self.DEBUG:
            print self.ys
            self.__output_dbg_img()

    def create_slices (self, min_height):
        '''makes the slics array, the image slices at the ys values'''
        self.slics = []

        for i in range(0, len(self.ys) - 1):
            if self.ys[i+1] - self.ys[i] > min_height:
                self.slics.append(self.img[self.ys[i]:self.ys[i+1], 0:self.img.shape[1]])

    def output_slices (self, prefix):
        '''write the slices to files: prefix#.jpg'''
        for i in range(0, len(self.slics)):
            cv2.imwrite(prefix + str(i) + ".jpg", self.slics[i])
