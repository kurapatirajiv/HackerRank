# https://www.hackerrank.com/challenges/np-dot-and-cross
import numpy
n = int(raw_input())
a,b = [],[]
for _ in range(n):
    a.append(map(int,raw_input().split()))
for _ in range(n):
    b.append(map(int,raw_input().split()))    
# Dot product of the elements result in matrix multiplication    
print numpy.dot(numpy.array(a),numpy.array(b))   