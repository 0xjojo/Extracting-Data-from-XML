import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
#from bs4 import BeautifulSoup
import ssl
sum = 0
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input("Enter location:")
print ("Retrieving" , url)
html = urllib.request.urlopen(url, context=ctx).read()
print ("Retrieved" , len(html) , "characters")
tree = ET.fromstring(html)
st = tree.findall('comments/comment')
print('Count:', len(st))
#lst = tree.findall('count')
#counts = tree.findall('.//count') different way to the same path
#print ("Count:" ,len(counts))
for item in st:
    #print('Name', item.find('name').text)
    #print('Count', item.find('count').text)
    x = item.find('count').text
    y = int(x)
    sum = sum + y
print ("Sum:",sum)
