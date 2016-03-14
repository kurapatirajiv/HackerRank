# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values
from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print tag
        if len(attrs)>0:
            for element in attrs:
                print "-> " + str(element[0]) + " > " + str(element[1])
inHtml = ""
for _ in range(int(raw_input())):
    inHtml = inHtml + raw_input()  
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(inHtml)


