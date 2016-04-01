import tornado.ioloop
import tornado.web

import os.path

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

settings = dict(template_path=os.path.join(os.path.dirname(__file__), "templates"), static_path=os.path.join(os.path.dirname(__file__), "static"), debug=True)

application = tornado.web.Application([(r"/", MainHandler)],**settings)

if __name__== "__main__":
    print "Server is running"
    print "ctrl +c to close"
    application.listen(8881)
    tornado.ioloop.IOLoop.instance().start()