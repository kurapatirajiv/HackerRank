# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/itertools-combinations
from itertools import combinations 
text,number = raw_input().split()
for x in range(int(number)):
    temp = []
    for y in sorted(list(combinations(text,x+1))):
        temp.append(sorted(y))
    print ('\n'.join(''.join(z) for z in sorted(temp)))    
    

  