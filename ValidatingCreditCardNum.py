# https://www.hackerrank.com/challenges/validating-credit-card-number
import re
for _ in range(int(input())):
    s = input()
    joinedStr = "".join(s.split("-"))
    # ^[4-6]{1}[0-9]{3} : starting with digits 4,5,6 on one char length,followed by digits 0-9 of length 3
    # -[0-9]{4} : starting with hyphen followed by digits 0-9 of length 4 OR
    # [0-9]{4}){3}$ : digits 0-9 of length 4 
    # (-[0-9]{4}|[0-9]{4}){3}$ : Above group is repeated 3 times as first 4 digits are covered
    # .*(.)\1{3} : Current character if matches with the next character and the set repeats 3 times ex:4444- then it is invalid
    # JoinedStr is passed to the .*(.)\1{3} after removing "-" because consecutive checking would be easier
    print('Valid' if (re.match(r'^[4-6]{1}[0-9]{3}(-[0-9]{4}|[0-9]{4}){3}$',s) and not re.search(r'.*(.)\1{3}',joinedStr)) else 'Invalid')