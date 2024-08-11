import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Specify paths
input_pdf_path = 'css.pdf'    # Replace with your input PDF file path
output_pdf_path = 'output_text_pdf.pdf'  # Path to save the output text PDF

# Open the original PDF
doc = fitz.open(input_pdf_path)

# Initialize a new PDF using ReportLab
packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
width, height = letter

# Iterate through each page in the PDF
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    
    # Render the page to an image
    pix = page.get_pixmap()
    
    # Save the image as a PNG in memory
    img_data = io.BytesIO(pix.tobytes(output="png"))
    img = Image.open(img_data)
    
    # Perform OCR on the image
    text = pytesseract.image_to_string(img)
    
    # Write the extracted text to the new PDF
    can.drawString(10, height - 40, f"Page {page_num + 1}")
    text_lines = text.splitlines()
    
    for i, line in enumerate(text_lines):
        can.drawString(10, height - 60 - 15 * i, line)
    
    can.showPage()  # Create a new page in the output PDF

can.save()

# Move to the beginning of the BytesIO buffer
packet.seek(0)

# Write the new PDF with OCR text
with open(output_pdf_path, 'wb') as output_pdf_file:
    output_pdf_file.write(packet.getvalue())

print(f"Text PDF saved as '{output_pdf_path}'")
