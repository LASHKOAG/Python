import xml.etree.ElementTree as ET
root = ET.parse('thefile.xml').getroot()

valueList=[]

for type_tag in root.findall('bar/type'):
    value = type_tag.get('foobar')
    print(value)
    valueList.append(value)

print ("\nList of parser value\n")
print(valueList)
