# https://www.hackerrank.com/challenges/html-parser-part-1
from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start :", tag
        if len(attrs)>0:
            for element in attrs:
                print "-> " + str(element[0]) + " > " + str(element[1])
    def handle_endtag(self, tag):
        print "End   :", tag
    def handle_startendtag(self, tag, attrs):
        print "Empty :", tag
        if len(attrs)>0:
            for element in attrs:
                print "-> " + str(element[0]) + " > " + str(element[1])
inHtml = ""
for _ in range(int(raw_input())):
    inHtml = inHtml + raw_input()  
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(inHtml)


