# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/python-string-formatting
# Hint : trinhhoangnhu user
n = int(raw_input());
wide = len("{0:b}".format(n));
for i in range(1,n+1):  
    print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=wide);
