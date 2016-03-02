# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/incorrect-regex
import re
for _ in range(int(raw_input())):
    try:
        re.compile(raw_input())
        print True
    except re.error:
        print False