# https://www.hackerrank.com/challenges/ginorts
# Hint : LittleFox user
# Mentioning the order
order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
# Sorted in the order of Index generated.
# "*" in print function is used to join all the elements in the list 
# Ex : without * ['g', 'i', 'n', 'o', 'r', 't', 'S', '1', '3', '2', '4']
# Ex : with    * ginortS1324
# "*" Operator compatible with Python 3 
print(*sorted(input(), key=order.index), sep='')