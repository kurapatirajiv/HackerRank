# https://www.hackerrank.com/challenges/introduction-to-regex
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
#Starting with + or - followed by (0..n)digits,one decimal point,(1...n) decimal digit mandatory
pattern = re.compile('^[+-]?\d*\.{1}\d+$')
for _ in range(int(raw_input())):
    print(True if(pattern.match(raw_input())) else False)
