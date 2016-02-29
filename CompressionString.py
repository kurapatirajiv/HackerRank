# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/compress-the-string
from itertools import groupby
for key,group in groupby(raw_input()):
    print (len(list(group)),int(key)),