# https://www.hackerrank.com/challenges/np-inner-and-outer
import numpy
a = numpy.array(map(int,raw_input().split()),int)
b = numpy.array(map(int,raw_input().split()),int)
print numpy.inner(a,b)
print numpy.outer(a,b)