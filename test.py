import tornado.ioloop
import tornado.web

import os.path

def main():
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8888)
    server.start(0)
    IOLoop.current().start()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

settings = dict(template_path=os.path.join(os.path.dirname(__file__), "templates"), static_path=os.path.join(os.path.dirname(__file__), "static"), debug=True)

application = tornado.web.Application([(r"/", MainHandler)],**settings)

if __name__== "__main__":
    main()