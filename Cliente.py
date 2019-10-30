from tornado.ioloop import IOLoop, PeriodicCallback
from tornado import gen
from tornado.websocket import websocket_connect


class Client(object):
    def __init__(self, url, timeout,msg):
        self.mensagem = msg
        self.url = url
        self.timeout = timeout
        self.ioloop = IOLoop.instance()
        self.ws = None
        self.connect()
	PeriodicCallback(self.keep_alive, 20000).start()
        self.ioloop.start()

    @gen.coroutine
    def connect(self):
        print "Tentando conectar"
        try:
            self.ws = yield websocket_connect(self.url)
        except Exception, e:
            print "Erro ao conectar"
        else:
            print "Conectado ao Servidor"
            self.run()

    @gen.coroutine
    def run(self):
        while True:
            msg = yield self.ws.read_message()
            if msg is None:
                print "Conexao Finalizada"
                self.ws = None
                break
                

    def keep_alive(self):
		
        if self.ws is None:
            self.connect()
        else:
            self.ws.write_message(self.mensagem)

if __name__ == "__main__":
	
	while True:
		msg =raw_input("Envie uma mensagem para o servidor: ")
		client = Client("ws://192.168.1.12:9000", 5,msg)
