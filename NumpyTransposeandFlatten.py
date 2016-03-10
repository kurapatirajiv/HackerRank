#https://www.hackerrank.com/challenges/np-transpose-and-flatten
import numpy
n,m = map(int,(input().split()))
myList = []
for _ in range(n):
    myList.append(list(map(int,input().split())))
myArray = numpy.array(myList)
#Columns to Rows convertion
print(numpy.transpose(myArray))
# Flatten in into a single dimension array with zero columns, single row
print(myArray.flatten())