# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/word-order
from collections import OrderedDict 
wordList = OrderedDict()
for _ in range(int(raw_input())):
    word = raw_input()
    wordList[word] = wordList.get(word,0) + 1
print wordList.__len__()
for i in wordList.values():
    print i,
               
               