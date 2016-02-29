# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/itertools-product
from itertools import product
A = list(map(int,raw_input().split()));
B = list(map(int,raw_input().split()));
result = list(product(A,B));
for x in result:
    #Prints the elements in a single line
    print x,