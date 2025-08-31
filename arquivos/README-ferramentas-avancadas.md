# 12. Ferramentas Avançadas

Este módulo cobre:
- Watcher de arquivos com `watchdog`
- Parsing de XML/HTML com `lxml` e `BeautifulSoup`
- Manipulação de PDFs com `PyPDF2` e `pdfplumber`
- Manipulação de imagens com `Pillow`
- Manipulação de áudio com `wave`, `pydub`, `soundfile`

## Exemplos
Veja o arquivo `ferramentas_avancadas.py` para funções práticas:
- `iniciar_watcher`: monitora alterações em arquivos
- `parse_xml` e `parse_html`: extrai dados de XML/HTML
- `ler_pdf`: extrai texto de PDF
- `abrir_imagem`: obtém tamanho de imagem
- `info_audio`: obtém informações de áudio

## Como rodar
1. Instale dependências:
   ```bash
   pip install watchdog lxml beautifulsoup4 PyPDF2 pdfplumber Pillow pydub soundfile
   ```
2. Execute exemplos adaptando conforme sua necessidade:
   ```bash
   python arquivos/ferramentas_avancadas.py
   ```

## Explicação
- Watchdog permite automação e monitoramento de arquivos.
- lxml e BeautifulSoup facilitam parsing de XML/HTML.
- PyPDF2/pdfplumber extraem dados de PDFs.
- Pillow manipula imagens.
- pydub/soundfile/wave manipulam áudio.

Referências:
- [watchdog](https://pypi.org/project/watchdog/)
- [lxml](https://lxml.de/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [pdfplumber](https://pypi.org/project/pdfplumber/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [pydub](https://pydub.com/)
- [soundfile](https://pysoundfile.readthedocs.io/en/latest/)
