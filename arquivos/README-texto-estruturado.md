# 3. Trabalhando com Texto Estruturado

Este módulo cobre:
- Manipulação de arquivos CSV, JSON, YAML, INI e .env
- Leitura e escrita de dados estruturados
- Conversão entre formatos

## Exemplos
Veja o arquivo `texto_estruturado.py` para funções de leitura e escrita:
- CSV: `ler_csv`, `escrever_csv`
- JSON: `ler_json`, `escrever_json`
- YAML: `ler_yaml`, `escrever_yaml`
- INI: `ler_ini`, `escrever_ini`
- .env: `ler_env`

## Como rodar
1. Instale dependências:
   ```bash
   pip install pyyaml python-dotenv
   ```
2. Execute exemplos adaptando conforme sua necessidade:
   ```bash
   python arquivos/texto_estruturado.py
   ```

## Explicação
- CSV: Para dados tabulares simples, compatível com Excel.
- JSON: Estrutura flexível, muito usado em APIs.
- YAML: Configuração legível, usado em DevOps e data science.
- INI: Configuração tradicional, fácil de editar.
- .env: Variáveis de ambiente, útil para segredos e configs.

### Conversão entre formatos
- Use as funções para ler de um formato e escrever em outro.
- Exemplo: converter CSV para JSON:
  ```python
  dados = ler_csv('dados.csv')
  escrever_json('dados.json', dados)
  ```

Consulte o arquivo para exemplos práticos e adapte conforme seu projeto.

Referências:
- [csv](https://docs.python.org/3/library/csv.html)
- [json](https://docs.python.org/3/library/json.html)
- [pyyaml](https://pyyaml.org/wiki/PyYAMLDocumentation)
- [configparser](https://docs.python.org/3/library/configparser.html)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
