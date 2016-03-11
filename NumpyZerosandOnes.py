# https://www.hackerrank.com/challenges/np-zeros-and-ones
import numpy
a = list(map(int,input().split()))
#Since we don't know the number of input parameters all are inserted into a list a and then passed
#First parameters is the number of times the array should be repeated
print (numpy.zeros(a,dtype = numpy.int))
print (numpy.ones(a,dtype= numpy.int))