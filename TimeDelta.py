#https://www.hackerrank.com/challenges/python-time-delta
# Note : since %z does not work in Python2 used Python3
# Reference : https://docs.python.org/2/library/datetime.html
from datetime import datetime
n = int(input());
while n >0:
    ts1 = input()
    ts2 = input()
    # strptime is used to convert the string date to Date type object
    diff = datetime.strptime(ts1, '%a %d %b %Y %H:%M:%S %z') - datetime.strptime(ts2, '%a %d %b %Y %H:%M:%S %z')
    print (abs(int(diff.total_seconds())));
    n = n - 1;