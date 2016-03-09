# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter
import re
l = []
regex = re.compile("^[\\w-]+@[a-zA-Z\\d]+\\.[a-zA-Z\\d]{1,3}$")
l = [input().strip() for _ in range(int(input()))]
print(sorted(list(filter(regex.match, l))))