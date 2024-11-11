import os

# Estrutura do projeto com arquivos e diretórios
project_structure = {
    "stj_jurisprudencia_extractor": [
        "JTSelecao_backup.pdf",                  # Arquivo PDF a ser convertido (não será criado)
        "output/",                               # Diretório para arquivos Markdown gerados
        "output/JTSelecao_backup.md",            # Arquivo Markdown gerado
        "README.md",                             # Instruções do projeto
        "requirements.txt",                      # Dependências do projeto
        ".gitignore",                            # Arquivos a serem ignorados pelo Git
        "src/",                                  # Diretório para o código Python
        "src/pdf_to_markdown.py",                # Script de conversão PDF -> Markdown
    ]
}

# Descrição dos arquivos e diretórios
description = """
Estrutura do projeto:
    
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
"""

# Função para criar a estrutura do diretório e arquivos
def create_project_structure(structure):
    base_path = os.path.join(os.getcwd(), "stj_jurisprudencia_extractor")
    os.makedirs(base_path, exist_ok=True)
    
    for path in structure["stj_jurisprudencia_extractor"]:
        full_path = os.path.join(base_path, path)
        
        # Verifica se é um diretório ou arquivo
        if path.endswith("/"):
            os.makedirs(full_path, exist_ok=True)
        else:
            # Cria o arquivo vazio
            with open(full_path, "w") as f:
                # Preenche o conteúdo de README.md, requirements.txt e .gitignore
                if path == "README.md":
                    f.write("# STJ Jurisprudência Extractor\n\nEste projeto converte PDFs de jurisprudências do STJ para Markdown.")
                elif path == "requirements.txt":
                    f.write("PyPDF2==3.0.0\nmarkdownify==0.9.3")
                elif path == ".gitignore":
                    f.write("venv/\n__pycache__/\n*.pyc\noutput/*.md")
                elif path == "src/pdf_to_markdown.py":
                    f.write("# Script de conversão de PDFs para Markdown\n")

    # Cria o arquivo de descrição
    with open(os.path.join(base_path, "project_description.txt"), "w") as f:
        f.write(description)

# Executa a criação da estrutura
create_project_structure(project_structure)
print("Estrutura de diretórios criada com sucesso!")
