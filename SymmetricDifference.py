# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/sets
noa = int(raw_input());
aset = set((map(int,raw_input().split())));
nob = int(raw_input());
bset = set((map(int,raw_input().split())));

#difference function finds the unique elements present in aset and not in the other
aunique = aset.difference(bset);
#difference function finds the unique elements present in bset and not in the other
bunique = bset.difference(aset);

#Sorted function sorts the sets
for x in sorted(aunique.union(bunique)):
    print x;