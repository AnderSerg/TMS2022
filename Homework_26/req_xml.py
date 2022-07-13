import xml.etree.ElementTree as ET

tree = ET.parse('library.xml')
root = tree.getroot()

for author in root:
    print(author.tag, author.attrib)

print(tree.find("book[author='Gambardella, Matthew']"))
