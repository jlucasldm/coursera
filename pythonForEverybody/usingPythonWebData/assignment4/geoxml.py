# Extracting Data from XML
# The program will prompt for a URL, read the XML data 
# from that URL using urllib and then parse and extract 
# the comment counts from the XML data, compute the sum 
# of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

som = 0

address = input('Enter location: ')
print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
counts = tree.findall('.//count')
    
for item in counts:
    #print('Count', item.text)
    som += int(item.text)

print(som)

