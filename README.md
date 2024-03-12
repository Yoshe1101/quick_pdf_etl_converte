# Python Virtual environment

install virtual env package: 
pip install virtualenv
pip install virtualenvwrapper

activate the virtual environment(windows): 
.pdf_elt_env\Scripts\Ativate-ps1

deactivate: 
deactivate

to run the script: python main.py



pyinstaller --name 'ETL_PDF_SPLITTER' \
            --icon 'yo.ico' \
            --windowed  \
            --add-data='./converter.py:.' \
            ui.py