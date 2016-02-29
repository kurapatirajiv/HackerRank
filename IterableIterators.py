# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/iterables-and-iterators
from itertools import combinations
number = raw_input()
favCases = 0
totalCases = 0
for x in list(combinations(''.join(raw_input().split()),int(raw_input()))):
    if 'a' in ''.join(x):
        favCases = favCases + 1;
    totalCases = totalCases + 1;
print float(favCases)/totalCases    