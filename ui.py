import tkinter as tk
from converter import PDFsplit 

def retrieve_input():
    input = self.myText_Box.get("How Many Jobs you want to run?",END)
    return int(input)

def on_submit():
    total_results = {}
    for i in range(100):
        row_results = []
        for j in range(5):
            text = entry_matrix[i][j].get()
            row_results.append(text)
        total_results[i] = row_results
    for i in total_results:
        for l in total_results[i]:
            if l == '':
                tk.messagebox.showinfo("SUCCESS!", "The files has been processed") 
                exit()
 
        a, b, c, d, e = total_results[i]
    
        PDFsplit(a,int(b),int(c),d,e)
    
                
            

# Create the main window
window = tk.Tk()
window.title("Scrollable Text Fields Matrix Example")

# Create a canvas with vertical scrollbar
canvas = tk.Canvas(window, scrollregion=(0, 0, 0, 6000))  # Adjust the scrollregion based on your content
canvas.grid(row=0, column=0, sticky="nsew")

# Create a frame inside the canvas to hold the text entry fields
inner_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# Create a matrix to store entry widgets
entry_matrix = []

# Create and place 100x6 matrix of text entry fields
for i in range(100):
    row_entries = []
    for j in range(5):

        if j == 0:
            texts = f"Job Nº{i+1}:  PDF location"
        elif j == 1:
            texts = "FROM:"
        elif j == 2:
            texts = "TO:"
        elif j == 3:
            texts = "Output Folder"
        else:
            texts = "Output Name"
        

        label = tk.Label(inner_frame, text=f"{texts} ")
        label.grid(row=i, column=j * 2, padx=10, pady=10, sticky=tk.W)

        entry = tk.Entry(inner_frame)
        entry.grid(row=i, column=j * 2 + 1, padx=10, pady=10, sticky=tk.W)

        row_entries.append(entry)

    entry_matrix.append(row_entries)

# Create and place vertical scrollbar
v_scrollbar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
v_scrollbar.grid(row=0, column=1, sticky="ns")
canvas.configure(yscrollcommand=v_scrollbar.set)

# Bind the frame size to the canvas viewport
inner_frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

# Create and place a submit button
submit_button = tk.Button(window, text="Submit", command=on_submit)
submit_button.grid(row=1, column=0, pady=10)

# Configure row and column weights for resizing
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Run the main loop
window.mainloop()
