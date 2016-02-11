# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/find-a-string
instr,insubstr  = raw_input(),raw_input();
count = 0;
for x in range(len(instr)-len(insubstr)+1):
    if (insubstr == instr[x:x+len(insubstr)]):
        count = count + 1;
print count;        


        