# https://www.hackerrank.com/challenges/matrix-script
import re
n,m = map(int,(input().split()))
inList = []
inMerge = []
# Code of converting columns to rows
for _ in range(n):
    inList.append(input()[:m])
for i in range(m):
    temp = ""
    for element in inList:
        temp = temp + element[i]  
    inMerge.append(temp) 
inStr = "".join(inMerge)
#inStr gives the flattened input
# (?<=\w) look behind assertion to verify if it has a word character before the special character
# (?=\w) look ahead assertion to verify it it has a word character after the special character
# ([^A-Za-z0-9]+) : Substitute all other than these chars which can be more than one
modStr = re.sub(r'(?<=\w)([^A-Za-z0-9]+)(?=\w)'," ",inStr)
print (modStr)