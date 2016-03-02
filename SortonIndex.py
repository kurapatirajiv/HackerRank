# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/python-sort-sort
from operator import itemgetter
n,m = map(int,raw_input().split())
result = []
for _ in range(n):
    result.append(map(int,raw_input().split()))
k = int(raw_input())
for element in sorted(result,key = itemgetter(k)):
    for item in element:
        print item,
    print "" 
        