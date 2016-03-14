# https://www.hackerrank.com/challenges/hex-color-code
# Bug : if the color code is invalid it still trims to the correct value and prints out :P
# Added \b to remove the bug which identifies end of a word is indicated by whitespace or a non-alphanumeric, non-    underscore character
import re
for _ in range(int(input())):
    # (?<!^) Matches if the current position in the string is not preceded by a match for a #
    # Characters should be 3 and 6 in length
    match = re.findall(r'((?<!^)#[0-9A-Fa-f]{6}|(?<!^)#[0-9A-Fa-f]{3})\b', input().strip(), flags = re.I)
    if match:
        print('\n'.join(match))