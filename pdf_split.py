from PyPDF2 import PdfReader, PdfWriter

# Load your existing PDF
input_pdf_path = 'css.pdf'  # Replace with your file path
output_pdf_path = 'css2.pdf'

# Define pages to extract (e.g., extract pages 1 and 2)
pages_to_extract = [0, 1]  # PyPDF2 uses zero-based indexing

# Create a PdfReader object
pdf_reader = PdfReader(input_pdf_path)

# Create a PdfWriter object for the new PDF
pdf_writer = PdfWriter()

# Add the specified pages to the writer
for page_number in pages_to_extract:
    pdf_writer.add_page(pdf_reader.pages[page_number])

# Write the new PDF to disk
with open(output_pdf_path, 'wb') as output_pdf_file:
    pdf_writer.write(output_pdf_file)

print(f"New PDF created: {output_pdf_path}")
