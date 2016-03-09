# https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Source Python docs
import xml.etree.ElementTree as etree
xml = ""
count = 0
for _ in range(int(raw_input())):
    xml = xml + raw_input()
tree = etree.ElementTree(etree.fromstring(xml))
class MaxDepth:                     # The target object of the parser
    maxDepth = 0
    depth = 0
    def start(self, tag, attrib):   # Called for each opening tag.
        self.depth += 1
        if self.depth > self.maxDepth:
            self.maxDepth = self.depth
    def end(self, tag):             # Called for each closing tag.
        self.depth -= 1
    def data(self, data):
         pass            # We do not need to do anything with data.
    def close(self):    # Called when all data has been parsed.
        # Since the feed tag is not be counted
         return self.maxDepth - 1
parser = etree.XMLParser(target=MaxDepth())
parser.feed(xml)
print parser.close()  

