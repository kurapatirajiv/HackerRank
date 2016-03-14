import re
for _ in range(int(input())):
    s = input()
    # [A-Za-z0-9]{10} : 10 letters of the given sequence
    # ([A-Z].*){2} : Matches any character with A-Z and accepts the value which are atleast two
    # ([0-9].*){3} : Matches any character with 0-9 and accepts the value which are atleast two
    # r'(.).*\1 : whatever character end up in the parentheses is matched against every other character in the string after it to make sure it repeats only once
    print('Valid' if all(re.search(r, s) for r in [r'[A-Za-z0-9]{10}',r'([A-Z].*){2}',r'([0-9].*){3}']) and not re.search(r'(.).*\1', s) else 'Invalid')