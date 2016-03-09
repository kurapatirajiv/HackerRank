# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators
# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function
phDir = []
postDecPhDir = []
for _ in range(int(input())):
      phDir.append(input())        
def decorate(phDir):
    for element in phDir:
        temp = "+91 " + element[-10:-5] + " " + element[-5:]
        postDecPhDir.append(temp)
    return postDecPhDir    
print (*sorted(decorate(phDir)),sep= '\n')