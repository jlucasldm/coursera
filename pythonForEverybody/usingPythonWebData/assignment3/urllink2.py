# Scraping Numbers from HTML using BeautifulSoup
# In this assignment you will write a Python program 
# similar to http://www.py4e.com/code3/urllink2.py. 
# The program will use urllib to read the HTML from 
# the data files below, and parse the data, extracting 
# numbers and compute the sum of the numbers in the file.

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
soma = 0

for tag in tags:
    tag = tag.decode()
    num = re.findall('[0-9]+', tag)
    #print(num)
    soma+= int(num[0])

print(soma)

# Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)
