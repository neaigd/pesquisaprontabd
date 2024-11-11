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