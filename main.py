import os
import PyPDF2
from PyQt5.QtWidgets import QApplication, QFileDialog
import sys

app = QApplication([])
files, _ = QFileDialog.getOpenFileNames(None, "Select PDF Files", os.path.expanduser("~"), "PDF Files (*.pdf)")

if not files:
    print("No files selected.")
    exit()

merged_pdf = PyPDF2.PdfMerger()

for file_name in files:
    try:
        with open(file_name, "rb") as pdf_file:
            merged_pdf.append(pdf_file)
            print(f"Added {file_name}")
    except IOError:
        print(f"Error opening {file_name}")

output_path = "merged.pdf"

try:
    with open(output_path, "wb") as merged_file:
        merged_pdf.write(merged_file)
    print(f"Merge successful. Output saved to {output_path}")
except IOError:
    print("Error saving merged PDF.")

sys.exit(app.exec_())
