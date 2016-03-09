# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/xml-1-find-the-score
import xml.etree.ElementTree as etree
xml = ""
count = 0
for _ in range(int(raw_input())):
    xml = xml + raw_input()
tree = etree.ElementTree(etree.fromstring(xml))
# To iterate through all the elements in a XML, returns the dictionary of elements
for node in tree.iter():
    # Count the dictionary elements
    count = count + len(node.attrib.items())
print count    