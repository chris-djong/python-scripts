from pdf2image import convert_from_path
import sys 
import os 

"""
 Script can be used to convert a specific pdf file into a png file 
 Takes the path to the pdf file as input - either a pdf file or a path where all pdf files are converted
 !!! Poppler needs to be installed. Use wsl environment -> apt-get install poppler-utils
"""

if (len(sys.argv) == 1):
    print("1 mandatory argument, pdf file")
    print("Please use 'python pdf2png.py /path/to/pdf' ")
    sys.exit()

def convert_pdf(document):
    print("Converting document", document)

    # Extract basename and pathname to save new pages
    name = os.path.basename(document)
    path = os.path.dirname(document)

    output_folder = os.path.join(path, name.replace(".pdf", "") + '-images')
    if (not os.path.exists(output_folder)):
        os.makedirs(output_folder)
    pages = convert_from_path(document)

    for i in range(len(pages)):
        
        pages[i].save(os.path.join(output_folder, name.replace('.pdf', f'-{i}.png')), 'PNG')
     


if (sys.argv[1].endswith('pdf')):
    convert_pdf(sys.argv[1])
else: 
    folder = sys.argv[1]
    for filename in os.listdir(folder):
        if (filename.endswith('.pdf')):
            convert_pdf(os.path.join(folder, filename))


