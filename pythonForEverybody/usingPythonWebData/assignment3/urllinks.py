# Following Links in Python
# The program will use urllib to read the HTML from 
# the data files below, extract the href= vaues from 
# the anchor tags, scan for a tag that is in a particular 
# position relative to the first name in the list, follow 
# that link and repeat the process a number of times and 
# report the last name you find.

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

pos = input('Enter the position - ')
times = input('Enter how many times the process will repeat - ')

# Retrieve all of the anchor tags
count = 0
stop = 0

while stop < int(times):
    tags = soup('a')
    
    for tag in tags:
        count+=1
        if count%int(pos) == 0:
            url = tag.get('href', None)
            html = urllib.request.urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            stop+=1
            break

name = re.findall('_by_([^ ]*).html', url)
print(name[0])

