# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/py-collections-ordereddict
from collections import OrderedDict
itemList = OrderedDict()
for _ in range(int(raw_input())):
    # Splits from right one time
    name,cost = raw_input().rsplit(" ",1)
    # Reads the cost adds it to the previous value, get function returns a valye of 0 by default
    itemList[name] = itemList.get(name,0) + int(cost);    
for i in itemList:
    print i,itemList[i]
    
    
