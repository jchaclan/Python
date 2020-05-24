import PyPDF2
from pathlib import Path
import sys

current_folder = Path("d:\\OneDrive - SQLI\\Perso\\Code\\python\\pdf\\")

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')



pdf_combiner(inputs)



# with open(f'{current_folder}\\dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     print(f'Number of pages: {reader.numPages}')

#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf','wb') as new_file:
#         writer.write(new_file)