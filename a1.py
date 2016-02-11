import datetime

Name = input("Enter your Name:")
age = int(input("Enter your Age:"))

current = int(datetime.date.today().year)
age = current + 100 - age 
print Name+" Will turn 100 at "+str(age)