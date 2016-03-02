# https://www.hackerrank.com/challenges/py-collections-deque
# Version : Python 3.0
from collections import deque
myQueue = deque()
for _ in range(int(input())):
    # *args length of arguments 0 to many
    command, *args = input().split()
    # command is applied to the queue 
    getattr(myQueue, command)(*args)
print (*myQueue)