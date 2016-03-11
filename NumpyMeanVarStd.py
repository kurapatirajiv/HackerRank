#https://www.hackerrank.com/challenges/np-mean-var-and-std
import numpy
n,m = map(int,raw_input().split())
myList = []
for _ in range(n):
    myList.append(map(int,raw_input().split()))
myArray = numpy.array(myList)    
print numpy.mean(myArray, axis=1)
print numpy.var(myArray,axis=0)
print numpy.std(myArray, axis=None)    