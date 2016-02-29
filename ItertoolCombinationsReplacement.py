# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement
from itertools import combinations_with_replacement
text,number = raw_input().split() 
print ('\n'.join(''.join(element) for element in list(combinations_with_replacement(sorted(text),int(number)))))