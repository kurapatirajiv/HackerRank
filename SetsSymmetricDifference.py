# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation
engCount = input();
stdEnglish = set(map(int,raw_input().split()));
frenchCount = input();
stdFrench = set(map(int,raw_input().split()));

print len(stdEnglish^stdFrench);
