import fitz  # PyMuPDF

def pdf_to_text(pdf_path, output_text_file):
    doc = fitz.open(pdf_path)
    text = ""

    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()

    doc.close()
    text = text.replace('\x0c', '') 
    text = text.replace('\n', '\n') 

    with open(output_text_file, 'w', encoding='utf-8') as file:
        file.write(text)

# Example usage
pdf_path = 'D:\Abdullah\pdfconverter\conference_paper.pdf'
output_text_file = 'output.txt'
pdf_to_text(pdf_path, output_text_file)
