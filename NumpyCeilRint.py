# https://www.hackerrank.com/challenges/floor-ceil-and-rint
import numpy
a = numpy.array(raw_input().split(),float)
#prints the rounded lower value than the given value 
print numpy.floor(a)
#prints the rounded upper value than the given value
print numpy.ceil(a)
#prints the rounded nearset integer value of the given value
print numpy.rint(a)