import tornado.web
import logging

log = logging.getLogger("AppHandler")
log.setLevel(logging.DEBUG)

class AppHandler(tornado.web.RequestHandler):
    def get(self):
        log.info('Hello ')
        self.render('index.html')
    
app = tornado.web.Application(handlers=[
    (r"/", AppHandler),
    (r"/assets/(.*)", tornado.web.StaticFileHandler, {"path": "assets/"})
])
