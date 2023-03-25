import pdfkit
file_names = ['nb1', '2', '3', '4']
for file_name in file_names: 
    pdfkit.from_file(f'notebook_htmls/{file_name}.html', f'notebook_pdfs/{file_name}.pdf')