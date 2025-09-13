from wsgiref.simple_server import make_server
from pathlib import Path


produtos = [
    {'name': 'Cadeira', 'price' : 123.49},
    {'name': 'Computaor', 'price': 34.32},
    {'name': 'Mouse', 'price': 48.33},
    {'name': 'Teclado', 'price': 32.43},
    {'name': 'Monitor', 'price': 9843.98},
]

def app(environment, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    
    produtos_html = ''
    for produto in produtos:
        produtos_html += f'<li>{produto['name']} R$ {produto['price']}.</li>'

    html = Path('index.html').read_text(encoding='utf-8')

    
    return [html.replace('{{PRODUTOS}}', produtos_html).encode('utf-8')]



make_server('', 5000, app).serve_forever()