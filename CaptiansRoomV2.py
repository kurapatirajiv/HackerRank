# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/py-the-captains-room
# Findin the unique element in a list
n = int(raw_input());
rooms = map(int,raw_input().split());
noofrooms = set(rooms);
sumofsets = sum(noofrooms)*n;
sumoflist = sum(rooms);
print (sumofsets-sumoflist)/(n-1);
        