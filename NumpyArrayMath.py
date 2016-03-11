# https://www.hackerrank.com/challenges/np-array-mathematics
import numpy
n,m = map(int,raw_input().split())
lista,listb = [],[]
for _ in range(n):
    lista.append(raw_input().split())
for _ in range(n):
    listb.append(raw_input().split())    
a = numpy.array(lista,dtype=numpy.int)
b = numpy.array(listb,dtype=numpy.int)
# adding a list into a list
print numpy.add(a,b)
print numpy.subtract(a,b)
print numpy.multiply(a,b)
print numpy.divide(a,b)
print numpy.mod(a,b)
print numpy.power(a,b)
