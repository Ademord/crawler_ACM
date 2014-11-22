import tornado.ioloop
import tornado.web
import tornado.template
import tornado.httpserver
import os
from user import User
from category import DP
import sys
loader = tornado.template.Loader(os.path.join(os.getcwd(), "templates"))

class Templates(object):
	#users list
	users_list = loader.load("prueba_movies_list.html")
	
class MainHandler(tornado.web.RequestHandler):
	def get(self):
		liAlex = User.getAcceptedIds("http://acm.timus.ru/author.aspx?id=124851")
		liAdemord = User.getAcceptedIds("http://acm.timus.ru/author.aspx?id=175581")
		liVudduu = User.getAcceptedIds("http://acm.timus.ru/author.aspx?id=106434")
		liJose = User.getAcceptedIds("http://acm.timus.ru/author.aspx?id=146721")
		li2 = DP.getProblemsIds()

		users = []
		accepted = [x for x in liAlex if x in li2]
		users.append({'name':'Alex', 'solved': len(accepted)})

		accepted = [x for x in liVudduu if x in li2]
		users.append({'name':'Vudduu', 'solved': len(accepted)})

		accepted = [x for x in liAdemord if x in li2]
		users.append({'name':'Ademord', 'solved': len(accepted)})

		accepted = [x for x in liJose if x in li2]
		users.append({'name':'Jose', 'solved': len(accepted)})
		
		html = Templates.users_list.generate(users = users)
		
		self.write(html)


def main():
	css_path = os.path.join(os.getcwd(), "templates","css")
	handlers = [ (r"/", MainHandler),
				(r'/css/(.*)', tornado.web.StaticFileHandler, {'path': css_path}) ]
	#settings = { "static_url": os.path.join(os.getcwd(), "templates", "css") }

	application = tornado.web.Application(handlers)
	http_server = tornado.httpserver.HTTPServer(application)
	port = int(os.environ.get("PORT", 5000))
	http_server.listen(port)
	tornado.ioloop.IOLoop.instance().start()
 
if __name__ == "__main__":
	main()