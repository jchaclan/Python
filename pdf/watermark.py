import PyPDF2
from pathlib import Path
import sys

current_folder = Path("d:\\OneDrive - SQLI\\Perso\\Code\\python\\pdf\\")

inputs = sys.argv[1:]

def getWatermark():
    reader = PyPDF2.PdfFileReader(open(f'{current_folder}\\wtr.pdf', 'rb'))
    page = reader.getPage(0)
    return page


def pdf_watermark(pdf_list,watermark):
    writer = PyPDF2.PdfFileWriter()
    for pdf in pdf_list:
        reader = PyPDF2.PdfFileReader(pdf)
        print(f'working with{pdf}')
        for page in reader.pages:
            page.mergePage(watermark)
            writer.addPage(page)
    with open('withWaterMark.pdf','wb') as new_file:
        writer.write(new_file)
    

watermark = getWatermark()
pdf_watermark(inputs,watermark)