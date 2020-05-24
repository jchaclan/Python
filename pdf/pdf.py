import PyPDF2
from pathlib import Path

current_folder = Path("d:\\OneDrive - SQLI\\Perso\\Code\\python\\pdf\\")

with open(f'{current_folder}\\dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(f'Number of pages: {reader.numPages}')

    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf','wb') as new_file:
        writer.write(new_file)

