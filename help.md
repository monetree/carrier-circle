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
	

	from lxml import html, etree
	from StringIO import StringIO
	html_string = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
	   "http://www.w3.org/TR/html4/loose.dtd">
	<html lang="en">
	<head/>
	<body>
	    <table border="1">
	      <tbody>
		<tr>
		  <td><a href="http://stackoverflow.com/foobar" title="Foobar">A link</a></td>
		</tr>
		<tr>
		  <td><a href="http://stackoverflow.com/baz" title="Baz">Another link</a></td>
		</tr>
	      </tbody>
	    </table>
	</body>
	</html>'''
	tree = etree.parse(StringIO(html_string))
	print tree.xpath('/html/body//tbody/tr/td/a[@title]/@href')
	>>> ['http://stackoverflow.com/foobar', 'http://stackoverflow.com/baz']




	import requests
	from bs4 import BeautifulSoup
	page = requests.get('http://www.freejobalert.com/upsc-advt-no-18/33742/')
	c = page.content
	soup = BeautifulSoup(c,"html.parser")
	row = soup.find_all('tr')
	dict = {}
	for i in row:
	    for title in i.find_all('span', attrs={
		'style':'color: #008000;'}):
		dict['Title'] = title.text
	    for link in i.find_all('a',attrs={'title':'UPSC'}, href=True):
		dict['Link'] = link['href']
		print(dict)




https://marcobonzanini.com/2015/02/25/fuzzy-string-matching-in-python/
