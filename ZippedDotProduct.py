# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/zipped
noOfStd,noOfSub = map(int,raw_input().split())
total = []
for _ in range(int(noOfSub)):
    total.append(list(map(float,raw_input().split())))
#Dot product of all elements in the list    
for item in zip(*total):
    avg = 0
    for element in item:
        avg = avg + element
    avg = avg/noOfSub
    print "%.1f" %avg    