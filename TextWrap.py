# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/text-wrap
import textwrap;
# Groups the string into the number given and prints vertically for fill and horizontally for wrap
print textwrap.fill(raw_input(),int(raw_input()));
