Para configurar o projeto de extração de texto e formatação em Markdown de PDFs de jurisprudências, como do STJ, vou detalhar cada etapa e componente no `README.md` que você vai rodar no VS Code. Incluirei o `requirements.txt` para as dependências do Python, o `.gitignore` para evitar o commit de arquivos indesejados, e outras instruções necessárias.

Aqui está o esboço do projeto inicial para você configurar:

### Estrutura do Projeto

```plaintext
stj_jurisprudencia_extractor/
│
├── JTSelecao_backup.pdf            # Seu arquivo PDF para conversão inicial
├── output/                         # Diretório para os arquivos Markdown gerados
│   └── JTSelecao_backup.md         # Arquivo Markdown gerado a partir do PDF
│
├── README.md                       # Instruções do projeto e dependências
├── requirements.txt                # Lista de pacotes Python necessários
├── .gitignore                      # Arquivos e pastas a serem ignorados pelo Git
└── src/                            # Diretório para o código Python
    └── pdf_to_markdown.py          # Script para converter PDFs para Markdown
```

---

### Conteúdo do `README.md`

```markdown
# STJ Jurisprudência Extractor

Este projeto converte arquivos PDF de jurisprudências do STJ em notas Markdown, mantendo links externos e formatação para facilitar o uso em ferramentas como o Obsidian. Ideal para advogados que desejam organizar referências e obter argumentos para petições.

## Funcionalidades

- Converte PDFs de jurisprudências para Markdown.
- Mantém os links externos para jurisprudências citadas.
- Identifica edições e seções específicas e organiza em um arquivo legível no formato Markdown.

## Configuração do Ambiente

### Requisitos

- **Python 3.8+**
- **pip** (para instalar as dependências)

### Passos para Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu_usuario/stj_jurisprudencia_extractor.git
    cd stj_jurisprudencia_extractor
    ```

2. Crie um ambiente virtual (recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate    # Para Linux/macOS
    venv\Scripts\activate       # Para Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

### Estrutura do Código

- `src/pdf_to_markdown.py`: script principal que faz a conversão de um arquivo PDF em um arquivo Markdown estruturado, preservando links externos.
- `output/`: diretório onde os arquivos Markdown convertidos serão salvos.

### Uso

1. Coloque o arquivo PDF que deseja converter na raiz do projeto.
2. Execute o script `pdf_to_markdown.py`:
    ```bash
    python src/pdf_to_markdown.py --input JTSelecao_backup.pdf --output output/JTSelecao_backup.md
    ```

O arquivo convertido aparecerá no diretório `output/`.

### Exemplo de Saída

O arquivo convertido manterá os títulos e links para as jurisprudências, ficando acessível no formato Markdown, pronto para ser importado para o Obsidian ou outra ferramenta de anotações.

## Desenvolvimento Futuro

O objetivo é expandir este projeto para converter múltiplos PDFs de uma vez e integrar com outras fontes de jurisprudências do STJ.

## Dependências

As dependências do projeto estão listadas no `requirements.txt`.

## Arquivos a serem Ignorados (.gitignore)

Inclui diretórios para ambiente virtual, arquivos de cache e saídas.

## Contribuindo

Contribuições são bem-vindas. Para contribuições, faça um fork do projeto e submeta um pull request.

```

### Conteúdo do `requirements.txt`

```plaintext
PyPDF2==3.0.0
markdownify==0.9.3
```

### Conteúdo do `.gitignore`

```plaintext
# Ignorar ambiente virtual
venv/
__pycache__/
*.pyc

# Ignorar arquivos de saída
output/*.md
```

### Código do `pdf_to_markdown.py`

No arquivo `pdf_to_markdown.py`, usaremos bibliotecas como `PyPDF2` para extrair o texto e `markdownify` para converter em Markdown. Abaixo está o script inicial:

```python
import re
import argparse
from PyPDF2 import PdfReader
import markdownify

def pdf_to_markdown(input_path, output_path):
    # Leitura do PDF
    reader = PdfReader(input_path)
    text_content = ""
    for page in reader.pages:
        text_content += page.extract_text()
    
    # Identificar edições, seções e links e transformar em markdown
    edition_pattern = r"(EDIÇÃO N\.\s*\d+:\s*DIREITO DO CONSUMIDOR\s*(I{0,3}))"
    content_blocks = re.split(edition_pattern, text_content)

    markdown_text = "# Jurisprudência em Teses\n\n"
    for idx, content in enumerate(content_blocks):
        if idx % 2 == 1:  # Título da Edição
            markdown_text += f"\n## {content.strip()}\n\n"
        elif idx % 2 == 0 and content.strip():  # Conteúdo da Edição
            # Substituir URLs com formato Markdown
            content_with_links = re.sub(r'(https?://\S+)', r'[\1](\1)', content)
            markdown_text += content_with_links + "\n\n"

    # Salvar arquivo Markdown
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(markdown_text)
    print(f"Arquivo convertido e salvo em: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Converter PDF para Markdown")
    parser.add_argument("--input", type=str, required=True, help="Caminho do arquivo PDF de entrada")
    parser.add_argument("--output", type=str, required=True, help="Caminho do arquivo Markdown de saída")
    args = parser.parse_args()

    pdf_to_markdown(args.input, args.output)
```

Esse é o código inicial. Ao expandir o projeto, será possível adicionar funcionalidades para processar múltiplos PDFs e otimizar o reconhecimento de padrões de jurisprudência.