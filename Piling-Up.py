# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/piling-up
from collections import deque
for i in range(int(raw_input())):
    cubeLength = int(raw_input())
    temp = []
    myQueue = deque(map(int,raw_input().split()))
    for _ in range(cubeLength):
	# Used logical operators rather than Max(a,b)  to use Popleft,pop functions use O(1). If we use Max we have to use remove which has O(n) as we don't know the position to delete(left,right)
        if myQueue[0] >= myQueue[-1]: 
            temp.append(myQueue[0])
            myQueue.popleft()
        else:
            temp.append(myQueue[-1])
            myQueue.pop()
        if temp[0] < temp[-1]:
            print "No"
            break
        if len(myQueue) == 0:
            print "Yes"
            
        
    
       
    
    
