from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import requests

class User(object):
	def getAcceptedIds(user_link):
		r = requests.get(user_link)
		#print(r.encoding)
		print("Crawling user...")
		r.encoding = 'cp1252'
		t = r.text
		s = BeautifulSoup(t)
		return [x.text for x in s.select('td.accepted > a')]
	#html = Templates.movies_list.generate(movies = accepted)
	#soup = BeautifulSoup(html)
	#print(soup)
