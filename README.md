# STJ Jurisprudência Extractor ⚖️📚

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange?style=flat-square)

Este projeto converte arquivos PDF de jurisprudências do STJ em notas Markdown, mantendo links externos e formatação para facilitar o uso em ferramentas como o Obsidian. Ideal para advogados que desejam organizar referências e obter argumentos para petições. 🧑‍⚖️📝

## ✨ Funcionalidades

-   Converte PDFs de jurisprudências para Markdown.
-   Mantém os links externos para jurisprudências citadas.
-   Identifica edições e seções específicas e organiza em um arquivo legível no formato Markdown.

## 🏗️ Estrutura do Projeto

```plaintext
stj_jurisprudencia_extractor/
│
├── 📄 JTSelecao_backup.pdf
├── 📁 output/
│   └── 📝 JTSelecao_backup.md
│
├── 📖 README.md
├── 📦 requirements.txt
├── 🚫 .gitignore
└── 📁 src/
    └── ⚙️ pdf_to_markdown.py
