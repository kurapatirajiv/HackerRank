# https://www.hackerrank.com/challenges/py-collections-namedtuple
from collections import namedtuple
avg,noOfStd,student =0, int(raw_input()),namedtuple('student', ' '.join(raw_input().split()))
for i in range(noOfStd):avg = avg + int(student._make(raw_input().split()).MARKS)
print "%.2f" % (float(avg)/noOfStd)