# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/py-set-add
n = int(raw_input());
result = set();
for i in range(0,n):
    result.add(raw_input());
    
print len(result);    