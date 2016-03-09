# https://www.hackerrank.com/challenges/decorators-2-name-directory
# We can also itemgetter() from operator module for using the for instead of the lambda function
# Did not structurally used Decorators
nameDir = []
for _ in range(int(input())):
    nameDir.append(input().split())
# Sort the key based on the age
for element in sorted(nameDir, key = lambda name: name[-2]):
    # Check for the gender in the last field and determine title of the Name
    # Join the first tow elements with a space between them i.e the First and Last name 	
    print ("Mr. " + " ".join(element[:-2]) if element[-1] == "M" else "Ms. " + " ".join(element[:-2]))