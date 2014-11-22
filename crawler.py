#import tornado.template
#import os
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import requests
#import sys
#loader = tornado.template.Loader(os.path.join(os.getcwd(), "templates"))

#class Templates(object):
	#users list
	#movies_list = loader.load("prueba_movies_list.html")
	
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
liAlex = User.getAcceptedIds("http://acm.timus.ru/author.aspx?id=124851")
liAdemord = User.getAcceptedIds("http://acm.timus.ru/author.aspx?id=175581")
liVudduu = User.getAcceptedIds("http://acm.timus.ru/author.aspx?id=106434")
liJose = User.getAcceptedIds("http://acm.timus.ru/author.aspx?id=146721")
li2 = DP.getProblemsIds()

accepted = [x for x in liAlex if x in li2]
print("Alex: ", len(accepted))

accepted = [x for x in liVudduu if x in li2]
print("Vudduu: ", len(accepted))

accepted = [x for x in liAdemord if x in li2]
print("Ademord: ", len(accepted))

accepted = [x for x in liJose if x in li2]
print("Jose: ", len(accepted))
