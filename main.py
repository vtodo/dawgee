import tornado.web
import logging
import json

log = logging.getLogger("AppHandler")
log.setLevel(logging.DEBUG)

class AppHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('dist/index.html', ip = self.request.remote_ip)
    
app = tornado.web.Application(handlers=[
    (r"/", AppHandler),
    (r"/assets/(.*)", tornado.web.StaticFileHandler, {"path": "dist/assets/"}),
    (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": "dist/js"}),
    (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": "dist/css/"})
])
