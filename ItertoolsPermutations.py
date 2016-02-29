# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/itertools-permutations
from itertools import permutations 
text,number = raw_input().split()
result= sorted(list(permutations(text,int(number))));
for x in result:
    output = ""
    #For the length of each tuple 
    for y in range(len(x)):
        output = output + x[y];
    print output    