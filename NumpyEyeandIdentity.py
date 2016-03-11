# https://www.hackerrank.com/challenges/np-eye-and-identity
import numpy
a,b = map(int,input().split())
# Default =0 is the main diagnal, the parameters expected by the function are integers and not a tuple
# Since the default array gives us float value numbers
print (numpy.eye(a,b,k=0))