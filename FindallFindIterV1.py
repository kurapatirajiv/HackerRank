# https://www.hackerrank.com/challenges/re-findall-re-finditer
import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
# (?<=['+c+']) for matching one consonant preceding the vowel
# (['+v+']{2,}) for collecting vowels with lenth 2 or more
# (?=['+c+']) followed by a consonant
# Flag is for ignoring the case
# The below regex will also filter spaces or any numerical characters
myList = map(lambda x: x.group(),re.finditer(r'(?<=['+c+'])(['+v+']{2,})(?=['+c+'])',raw_input(),flags=re.I))
if (len(myList)>0):
    for item in myList: print item
else: print "-1"        