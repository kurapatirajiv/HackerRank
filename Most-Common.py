# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/most-commons
from collections import OrderedDict
myList = OrderedDict()
for item in raw_input():
    myList[item] = myList.get(item,0) + 1
i = 0
# Reverse is set to true, because the sort function sorts the list in increasing order
# The list is internally sorted to support the requirements of printing the elements in alphabetical order
for item in sorted(sorted(myList),key=myList.get, reverse=True):
    if i < 3: print item, myList[item]; i = i + 1