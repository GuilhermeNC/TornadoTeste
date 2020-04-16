import os
import tornado.web
import tornado.ioloop

class staticRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

if __name__ == "__main__":
    app = tornado.web.Application({
        (r"/", staticRequestHandler)
    })

    app.listen(8881)
    print("Estou funcionando na porta 8881")
    tornado.ioloop.IOLoop.current().start()