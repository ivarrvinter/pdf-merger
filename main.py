import os
import PyPDF2
from PyQt5.QtWidgets import QApplication, QFileDialog


app = QApplication([])
files, _ = QFileDialog.getOpenFileNames(None, "Select PDF Files", os.path.expanduser("~"), "PDF Files (*.pdf)")
merged_pdf = PyPDF2.PdfMerger()

for file_name in files:
    with open(file_name, "rb") as pdf_file:
        merged_pdf.append(pdf_file)

with open("merged.pdf", "wb") as merged_file:
    merged_pdf.write(merged_file)
