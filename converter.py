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

def PDFsplit(pdf, initial_page ,final_page, output, name):
    if pdf == '':
        exit()
  # creating input pdf file object
    splits = []
    for i in range(initial_page, final_page):
        splits.append(i)

    
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

def main(file_path ,initial_page ,final_page, output_folder, output_name):


    pdf = file_path #get_path()
    output = output_name #output_folder()


    # store data in pdfReader
    pdfReader = PyPDF2.PdfReader(pdf)
  
    # count number of pages
    totalPages = len(pdfReader.pages)
    print(totalPages)

    number = 0
    units = 1
    lesson = 1
    for i in range(7,totalPages, 2):

        if lesson > 5:
            lesson = 1
            units = units + 1

        base_name =os.path.basename(pdf)

        print('{} of {}'.format(number, int(totalPages/2)))

        base_name = os.path.splitext(base_name)[0]

        name = '{}_unit_{}_point_{}.pdf'.format(base_name,units,lesson)          #  base_name + '_' +  '' + '.pdf'
        output = output + "/"
        lesson = lesson + 1
        splits = list()
        splits.append(i)     
        splits.append(i+1)
        PDFsplit(pdf, splits, output, name)
        number = number + 1


#if __name__ == "__main__":
#    main()