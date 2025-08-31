# pip install watchdog lxml beautifulsoup4 PyPDF2 pdfplumber Pillow pydub soundfile
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from lxml import etree
from bs4 import BeautifulSoup
import PyPDF2
import pdfplumber
from PIL import Image
import wave
import pydub
import soundfile as sf
import time

# Watcher de arquivos
def iniciar_watcher(pasta):
    class Handler(FileSystemEventHandler):
        def on_modified(self, event):
            print(f'Modificado: {event.src_path}')
    observer = Observer()
    observer.schedule(Handler(), pasta, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Parsing XML/HTML
def parse_xml(xml_str):
    root = etree.fromstring(xml_str)
    return root.tag

def parse_html(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    return soup.title.string if soup.title else None

# PDFs
def ler_pdf(caminho):
    with pdfplumber.open(caminho) as pdf:
        return pdf.pages[0].extract_text()

# Imagens
def abrir_imagem(caminho):
    img = Image.open(caminho)
    return img.size

# Áudio
def info_audio(caminho):
    data, samplerate = sf.read(caminho)
    return len(data), samplerate

# Exemplos no README-ferramentas-avancadas.md
