# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/py-collections-deque
from collections import deque
myQueue = deque()
for _ in range(int(raw_input())):
    invalue = raw_input();
    count = len(invalue.split()); 
    command = invalue.split();
    if ((count == 2 ) and (command[0] == "append")):
        myQueue.append(int(command[1]));
    elif ((count == 2) and (command[0] == "appendleft")):
        myQueue.appendleft(int(command[1]));
    elif ((count == 1) and (command[0] == "pop")):
        myQueue.pop();
    elif ((count == 1) and (command[0] == "popleft")):
        myQueue.popleft();    
    else:   
        print "Invalid Command";
for element in myQueue:
    print element,
    