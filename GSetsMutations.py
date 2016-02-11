# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/py-set-mutations
# Use of getattr method instead of nested if
no, result,n  = input(),set(raw_input().split()), input()

for _ in range(n):
    command = raw_input().split();
    getattr(result,command[0])(set(raw_input().split()));
    
print sum(map(int,result))
  
    