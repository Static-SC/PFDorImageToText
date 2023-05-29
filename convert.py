import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader
import pytesseract
from PIL import Image
import os

def image_to_text(image_path):
    with Image.open(image_path) as image:
        text = pytesseract.image_to_string(image)
        return text

def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        num_pages = len(reader.pages)
        text = ""

        for page in range(num_pages):
            pdf_page = reader.pages[page]
            text += pdf_page.extract_text()

        return text

# Create Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Prompt the user to select a file
file_path = filedialog.askopenfilename(initialdir="./", title="Select a file", filetypes=[("All Files", "*.jpg;*.jpeg;*.png;*.pdf"), ("PDF files", "*.pdf"), ("Image Files", "*.jpg;*.jpeg;*.png")])

if file_path:
    if file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
        # Convert image to text
        converted_text = image_to_text(file_path)
        output_file_path = "Image.txt"
    elif file_path.lower().endswith('.pdf'):
        # Convert PDF to text
        converted_text = pdf_to_text(file_path)
        output_file_path = "PDF.txt"
    else:
        print("Unsupported file format.")
        exit(1)

    # Write the converted text to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(converted_text)

    print(f"Conversion completed and saved to {output_file_path}")
else:
    print("No file selected.")
