import PyPDF2
import sys

path = sys.argv[1]
watermark = sys.argv[2]
output_path = sys.argv[3]

template = PyPDF2.PdfFileReader(open(path, 'rb'))
watermark = PyPDF2.PdfFileReader(open(watermark, 'rb'))

output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0)) # mergePage(), merged die pdfs richtig, nicht wie PyPdfFileMerger
    output.addPage(page)

    with open(output_path, 'wb') as file:
        output.write(file)
