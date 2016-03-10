#https://www.hackerrank.com/challenges/np-shape-reshape
import numpy
myArray = numpy.array(input().split(),int)
myArray.shape = (3,3)
print (myArray)