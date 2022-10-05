from PyPDF2 import PdfFileWriter, PdfFileReader
import os
from tkinter import filedialog



document = filedialog.askopenfilename(title='Please chose a pdf file')
# Extract basename and pathname to save new pages
name = os.path.basename(document)
path = os.path.dirname(document)

# Open the pdf reader
inputpdf = PdfFileReader(open(document, "rb"))
output_folder = os.path.join(path, 'pages-' + name)

# Create the folder to split the pages
if (not os.path.exists(output_folder)):
    os.makedirs(output_folder)

# And split it into pages
for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    page_path = os.path.join(output_folder, 'Page-%s.pdf' % (i+1))

    with open(page_path, "wb") as outputStream:
        output.write(outputStream)