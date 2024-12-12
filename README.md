# PDF Playground

Welcome to the PDF Playground! This repository contains a collection of Python scripts to manipulate PDF files using the PyPDF2 and PyMuPDF (fitz) libraries. These scripts demonstrate various PDF processing tasks, including rotation, watermarking, merging, and converting PDF pages to images.

## Features

1. **PDF Rotation:** Rotate PDF pages programmatically.
2. **PDF Watermarking:** Add watermarks to PDF files.
3. **PDF Merging:** Merge multiple PDF files into a single document.
4. **PDF to JPG Conversion:** Convert PDF pages to JPG images.

## Scripts

### 1. PDF Rotation (pdf.py)

**Description:** Rotate PDF pages programmatically.

**Usage:**

python pdf.py input_file.pdf output_file.pdf rotation_angle --password [optional]

### 2. PDF Watermarking (pdf-wtrmark.py)

**Description:** Add a watermark to PDF files.

**Usage:**

python pdf-wtrmark.py input_file.pdf output_file.pdf watermark_file.pdf --pages [optional] --password [optional]

### 3. PDF Merging (pdf-merger.py)

**Description:** Merge multiple PDF files into one.

**Usage:**

python pdf-merger.py pdf_file1.pdf pdf_file2.pdf ... output_file.pdf --password [optional]

### 4. PDF to JPG Conversion (pdf-jpg-converter.py)

**Description:** Convert PDF pages to JPG images.

**Usage:**

python pdf_to_jpg.py input_file.pdf output_folder

### Requirements

Python 3.x

PyPDF2

PyMuPDF (fitz)

argparse (standard library)

Installation
Install the required libraries using pip:

sh
pip install PyPDF2 PyMuPDF


### License

This project is licensed under the MIT License. See the LICENSE file for details.