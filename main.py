from bs4 import BeautifulSoup
import re

with open('my_playlist.html', 'r') as myfile:
    data=myfile.read().replace('\n', '')

soup = BeautifulSoup(data, features="html.parser")

index = 0
artist = ""
song = ""

for item in soup.findAll('span', attrs={'class':"column-content tooltip"}):
	# print(item.find('a', attrs={"aria-label":re.compile("Artist")}))
	if index == 0:
		song = item.text
	if index == 1:
		artist = item.text
	if index == 2:
		print(song+" - "+artist+" - "+item.text)
	index += 1
	if index == 3:
		index = 0
	# print(item.find('a', attrs={"aria-label":"Album"}).text)