# https://www.hackerrank.com/challenges/html-parser-part-2
from HTMLParser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_comment(self,data):
        print ">>> Multi-line Comment \n"+ data if "\n" in data else ">>> Single-line Comment \n" + data
    def handle_data(self,data):
        if (data != "\n"):
            print ">>> Data \n" + data
html = ""       
for i in range(int(raw_input())):
    html += raw_input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
