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

from lxml import html

sample = '<?xml version="1.0" encoding="UTF-8"?><root><a class="asig">I am the correct one.</a><a class="asig drcha">I am the wrong one.</a></root>'
tree = html.fromstring(sample)
print tree.xpath("//a[@class='asig']/text()")[0]
print tree.cssselect("a[class='asig']")[0].text
