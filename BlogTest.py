import tornado.web
import logging

log = logging.getLogger("blogTest")
log.setLevel(logging.DEBUG)

class HelloWorldHandler(tornado.web.RequestHandler):
    def get(self):
        log.info('Hello ')
        self.render('index.html')
    
app = tornado.web.Application(handlers=[
    (r"/", HelloWorldHandler),
    (r"/assets/(.*)", tornado.web.StaticFileHandler, {"path": "assets/"})
])
