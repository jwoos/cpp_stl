from bs4 import BeautifulSoup
import requests

html_get = requests.get('http://www.w3schools.com/tags/ref_color_tryit.asp')
html = html_get.text
html_soup = BeautifulSoup(html, 'html.parser')

tr = html_soup.find_all('tr')
tr.pop(0)

colors = []

for things in tr:
	new_string = things.contents[0].find('b').contents[0].replace(' ', '')
	colors.append(new_string)

with open('colors.txt', 'a') as open_file:
	for i in colors:
		open_file.write('"' + i + '"' + ',')
