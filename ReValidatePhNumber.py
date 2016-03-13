# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/validating-the-phone-number
import re
for _ in range(int(raw_input())):
    print "YES" if(re.match(r'^[7-9]\d{9}$',raw_input())) else "NO"