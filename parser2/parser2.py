import xml.etree.ElementTree as ET
root = ET.parse('thefile2.xml').getroot()

valueList=[]

for type_tag in root.findall('metadata/parameter'):
    value = type_tag.get('VAR')
    print(value)
    valueList.append(value)

print ("\nList of parser value\n")
print(valueList)
