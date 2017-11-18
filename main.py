import tornado.web
import logging
import json

log = logging.getLogger("AppHandler")
log.setLevel(logging.DEBUG)

cl = []
class AppHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('dist/index.html', ip = self.request.remote_ip, clients = len(cl))
    
class SocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        if self not in cl:
            cl.append(self)

    def on_close(self):
        if self in cl:
            cl.remove(self)

app = tornado.web.Application(handlers=[
    (r"/", AppHandler),
    (r"/ws", SocketHandler),
    (r"/assets/(.*)", tornado.web.StaticFileHandler, {"path": "dist/assets/"}),
    (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": "dist/js"}),
    (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": "dist/css/"})
])
