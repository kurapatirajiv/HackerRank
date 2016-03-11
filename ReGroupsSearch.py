# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/re-group-groups
import re
# \1 refers to the first and only matching group in the list
m = re.search(r'([a-zA-Z0-9])\1+', raw_input().strip())
print(m.group(1) if m else "-1")