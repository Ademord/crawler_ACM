from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import requests

class DP(object):
	def getProblemsIds():
		r = requests.get("http://acm.timus.ru/problemset.aspx?space=1&tag=dynprog")
		#print(r.encoding)
		r.encoding = 'cp1252'
		t = r.text
		bs = BeautifulSoup(t)
		return [x.text for x in bs.select('tr.content > td')[1::6]]
	
	def print_File(li):
		f = open('workfile_dp.txt', 'w')
		for x in li:
			print(x, file=f)
	#html = Templates.movies_list.generate(movies = accepted)
	#soup = BeautifulSoup(html)
	#print(soup)
