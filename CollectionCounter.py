# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/collections-counter
from collections import Counter
n = int(raw_input())
shoes = list(map(int,raw_input().split()))
moneyEarned = 0;
for _ in range(int(raw_input())):
    size,price = map(int,(raw_input().split()))
    if size in Counter(shoes).keys():
        moneyEarned = moneyEarned + price
        shoes.remove(size)
print moneyEarned        