# Extracting Data from JSON

# The program will prompt for a URL, read the JSON data from 
# that URL using urllib and then parse and extract the 
# comment counts from the JSON data, compute the sum of 
# the numbers in the file and enter the sum below:
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.json 
# (Sum=2553)

# Actual data: http://py4e-data.dr-chuck.net/comments_691884.json 
# (Sum ends with 97)

import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
comments = info["comments"]
som = 0

for item in comments:
    # print("Count:",item["count"])
    som += item["count"]

print(som)
