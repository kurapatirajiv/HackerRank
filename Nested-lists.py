# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/nested-list
n = int(raw_input());
stds = []
marklist = []
# Reading all the input into a 2D matrix
while(n>0):
    name  = raw_input();
    marks = float(raw_input());
    stds.append([name,marks]);
    if(marks not in marklist):
        marklist.append(marks);
    n = n - 1;
# Sorting the array to find the lowest number    
marklist.sort();
# Finding the second lowest number
lowestmark = marklist[1];    
result = [];

for i in range(len(stds)):
    if (stds[i][1] == lowestmark):
        result.append(stds[i][0]);
# Had to sort the list because of Testcase 1
result.sort();
for x in result:
    print x;
    
    