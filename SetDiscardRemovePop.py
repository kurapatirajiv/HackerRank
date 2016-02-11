# https://www.hackerrank.com/challenges/py-set-discard-remove-pop
no = input();
s = set(map(int, raw_input().split()))
n = int(raw_input());
while (n>0):
    invalue = raw_input();
    count = len(invalue.split()); 
    command = invalue.split();
    if ((count == 2 ) and (command[0] == "remove")):
        s.remove(int(command[1]));
    elif ((count == 2) and (command[0] == "discard")):
        s.discard(int(command[1]));
    elif ((count == 1) and (command[0] == "pop")):
        s.pop();
    else:   
        print "Invalid Command";
    n = n-1;

print sum(s);    
    