# pdf-invoice-extractor

A Python CLI tool that extracts invoice dates, document numbers, and total amounts from PDF files and exports them into an Excel spreadsheet.

## Features
- Reads text-based PDF files from a specified folder using PyMuPDF (fitz).
- Extracts key fields (date, document/invoice number, and total amount) using regular expressions.
- Exports structured results to an .xlsx file using pandas.
## Requirements
- Python 3.9+
- pymupdf
- pandas
- openpyxl
- ## Usage
Update the target folder and output filename in invoice_extractor.py, then run:

```bash
python invoice_extractor.py
