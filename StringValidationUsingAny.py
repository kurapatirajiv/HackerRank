# Enter your code here. Read input from STDIN. Print output to STDOUT

str = raw_input()
print any(c.isalnum()  for c in str)
print any(c.isalpha() for c in str)
print any(c.isdigit() for c in str)
print any(c.islower() for c in str)
print any(c.isupper() for c in str)
