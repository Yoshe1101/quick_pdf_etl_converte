import tkinter as tk
from converter import *
import pandas as pd

main_document = get_path()

df = pd.read_csv(main_document)

for i in range(df.shape[0]):
    extract = df.iloc[i]
    PDFsplit(extract["Source File"], extract["From"] ,extract["To"], extract["Destination"], extract["Name"])
