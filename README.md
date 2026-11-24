# pdf-invoice-extractor

A Python CLI tool that extracts invoice dates, document numbers, and total amounts from PDF files and exports them into an Excel spreadsheet.

## Features
- Reads text-based PDF files from a specified folder using PyMuPDF (fitz).
- Extracts key fields (date, document/invoice number, and total amount) using regular expressions.
- Exports structured results to an .xlsx file using pandas.

## Requirements
- Python 3.9+
- pymupdf>=1.24.0
- pandas>=2.0.0
- openpyxl>=3.1.0

## Installation
Install the required dependencies:
bash
pip install -r requirements.txt


## Usage
1. Place your text-based .pdf invoice files inside the target folder (default: ./ornek_faturalar).
2. Update the folder path or output filename in invoice_extractor.py if needed.
3. Run the script:

bash
python invoice_extractor.py


The output will be saved as faturalar.xlsx in the working directory.
