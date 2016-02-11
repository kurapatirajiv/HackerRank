# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/py-the-captains-room
# Findin the unique element in a list
n = raw_input();
rooms = map(int,raw_input().split());
noofrooms = set(rooms);
for i in noofrooms:
    rooms.remove(i);
    if i not in rooms:
        print i;
        

# The problem times out
# Different logic [sum(set(list))*K - sum(list elements)] (k-1)
# n*(k-1)/(k-1) gives N so it works on that formula
