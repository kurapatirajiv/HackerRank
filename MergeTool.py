# https://www.hackerrank.com/challenges/merge-the-tools
# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function
inStr = raw_input()
k = int(raw_input())
i,result = 0,[];
output = "";
for x in inStr:
    if i < k:
        if x not in result:
            print(x,end="")
            result.append(x)
    else:
        i = 0
        result = []
        result.append(x)
        print("\n"+x,end="")
    i = i + 1    