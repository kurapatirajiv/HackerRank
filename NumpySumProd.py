# https://www.hackerrank.com/challenges/np-sum-and-prod
import numpy
n,m = map(int,raw_input().split())
myList = []
for _ in range(n):
    myList.append(map(int,raw_input().split()))
print numpy.product(numpy.sum(numpy.array(myList), axis=0))