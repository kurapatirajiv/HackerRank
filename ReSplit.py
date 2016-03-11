# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/re-split
import re
#if condition is added to remove empty elements and then a new line character is added
print("\n".join(element for element in re.split(r'[\,\.]',input()) if len(element)>0))