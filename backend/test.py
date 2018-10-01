from lxml import html
from lxml import etree
import requests
page = requests.get('http://www.freejobalert.com/upsc-advt-no-17/31908/')
tree = html.fromstring(page.content)
tables = tree.cssselect('table')
file = open("output.html","wb") 
for table in tables:
    file.write(etree.tostring(table))


from lxml import html
from lxml import etree
import requests
page = requests.get('http://www.freejobalert.com/upsc-advt-no-17/31908/')
tree = html.fromstring(page.content)
tables = tree.xpath('//table')
file = open("output.html","wb") 
for t in tables:
	print(etree.tostring(t))
	file.write(etree.tostring(t))
