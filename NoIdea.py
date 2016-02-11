# Enter your code here. Read input from STDIN. Print output to STDOUT
# Sets eliminate duplicates
# https://www.hackerrank.com/challenges/no-idea
asize,setsize = raw_input().split();
array = map(int,raw_input().split());
seta,setb = set(map(int,raw_input().split())),set(map(int,raw_input().split()));
happy = 0;

for i in array:
    if i in seta:
        happy = happy + 1;
    if i in setb:
        happy = happy - 1;
        
print happy;