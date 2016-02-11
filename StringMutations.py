# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/python-mutations
instr = raw_input();
result = "";
pos,letter = raw_input().split();
pos = int(pos);
result = instr[:pos] + letter + instr[pos+1:];

print result;