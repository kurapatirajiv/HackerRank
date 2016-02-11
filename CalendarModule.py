# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/calendar-module
import calendar;
mm,dd,yyyy = map(int,(raw_input().split()));
print str(calendar.day_name[calendar.weekday(yyyy,mm,dd)]).upper();