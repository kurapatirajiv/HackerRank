#!/usr/bin/python
import sys
print "Argument", sys.argv
script,count = sys.argv

file=open("Done.txt","r+")
wordcount={}

count = int(count)
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
# for k,v in wordcount.items():
#    print k,":>>", v
print "words with greater count:", count
for l,r in wordcount.items():
    if (r >= count):
       if (len(str(l)) > 3):
           print l,r
