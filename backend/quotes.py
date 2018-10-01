
from lxml import html
import requests
page = requests.get('http://www.freejobalert.com/upsc-advt-no-17/31908/')
tree = html.fromstring(page.content)
tables = tree.xpath('p[1]/text()')[0]
print(tables)
