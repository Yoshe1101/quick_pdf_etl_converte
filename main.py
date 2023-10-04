import tkinter as tk
from tkinter import filedialog
import os
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter


def get_path():

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(initialdir='.')
    print(file_path)

    return file_path

def output_folder():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askdirectory(initialdir='.')
    print(file_path)

    return file_path

def PDFsplit(pdf, splits, output, name):
  # creating input pdf file object
    pdf_file_path = pdf
    file_base_name = output

    pdf = PdfReader(pdf_file_path)
    pages = splits #[0, 2, 4] # page 1, 3, 5
    pdfWriter = PdfWriter()

    for page_num in pages:
        pdfWriter.add_page(pdf.pages[page_num])

    with open(os.path.join(output, name), 'wb') as f:
        pdfWriter.write(f)
        f.close()
 
    # closing the input pdf file object
    #pdfFileObj.close()

def main():


    pdf = get_path()
    output = output_folder()


    # store data in pdfReader
    pdfReader = PyPDF2.PdfReader(pdf)
  
    # count number of pages
    totalPages = len(pdfReader.pages)
    print(totalPages)

    number = 0
    for i in range(0,totalPages, 2):
        print('{} of {}'.format(number, int(totalPages/2)))
        name = 'output_' + str(number) + '.pdf'
        splits = list()
        splits.append(i)     
        splits.append(i+1)
        PDFsplit(pdf, splits, output, name)
        number = number + 1


if __name__ == "__main__":
    main()