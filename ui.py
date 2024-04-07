from tkinter import *
from converter import *
import pandas as pd
from tkinter import messagebox



main_document = get_path()
cols = ['Notes',
        'Source File',
        'From',
        'To',
        'Destination',
        'Name'
        ]

df = pd.read_csv(main_document, sep=';')
print(df.to_string())

for i in range(df.shape[0]):
    extract = df.iloc[i]

    print("//////////////")

    #try:
    PDFsplit(extract["Source File"], extract["From"] ,extract["To"], extract["Destination"], extract["Name"])
    

    # except:
    #     win = Tk()

    #     # Set the size of the tkinter window
    #     win.geometry("400x200")

    #     # Define a function to show the error message
    #     def on_click():
    #         exit()

    #         # Create a label widget
    #     label = Label(win, text="Sorry, something went wrong, call you IT friend ",
    #     font=('Calibri 15 bold'))
    #     label.pack(pady=20)


    #         # Create a button to delete the button
    #     b = Button(win, text="Click Me", command=on_click)
    #     b.pack(pady=20)

    #     win.mainloop()
