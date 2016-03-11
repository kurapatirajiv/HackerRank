#https://www.hackerrank.com/challenges/np-min-and-max
import numpy
n,m = map(int,raw_input().split())
myList = []
for _ in range(n):
    myList.append(map(int,raw_input().split()))
print numpy.max(numpy.min(numpy.array(myList), axis=1))    
    