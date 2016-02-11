# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/
n = int(raw_input());
list = map(int,raw_input().split());
noduplist = [];
#Removing duplicates
for x in list:
    if x not in noduplist:
        noduplist.append(x);
#Sorting the list in ascending order        
noduplist.sort();
length = len(noduplist);
print noduplist[length-2];