# Fundamentos da Web em Python

# Cliente/Servidor
# Exemplo simples de servidor HTTP embutido
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>Olá, Web!</h1>')

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), SimpleHandler)
    print('Servidor rodando em http://localhost:8080')
    server.serve_forever()

# Para testar: python web/fundamentos_web.py
