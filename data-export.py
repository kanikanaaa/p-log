# export the above output, both statistics and visualization, to a pdf file using pypdfium2
!pip install fpdf2 reportlab
!pip install pypdfium2

from fpdf import FPDF
from PIL import Image

# Ensure pypdfium2 is imported for PDF generation (though fpdf2 is used here)
# import pypdfium2 as pdfium # Not strictly needed for this fpdf2 approach

# Define the output PDF path
output_pdf_path = 'drive/MyDrive/p-log/' + filename + '-report.pdf'

# Create a PDF object
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
# Japanese font
# downloaded from https://moji.or.jp/ipafont/ipa00303/
font_path =r"drive/MyDrive/p-log/ipag.ttf"
pdf.add_font("ipa",fname=font_path,uni=True)
pdf.set_font("ipa", size = 10)

# Add the combined image
combined_image_path = 'drive/MyDrive/p-log/'+ filename +'-all_visualizations.png'
try:
    # Get image dimensions to fit within PDF page width
    img = Image.open(combined_image_path)
    img_width, img_height = img.size
    pdf_width = pdf.w - 2*pdf.l_margin
    img_ratio = img_height / img_width
    pdf_height = pdf_width * img_ratio

    # Ensure image doesn't exceed page height (optional, but good practice)
    if pdf_height > pdf.h - 2*pdf.t_margin:
        pdf_height = pdf.h - 2*pdf.t_margin
        pdf_width = pdf_height / img_ratio


    pdf.image(combined_image_path, x = pdf.l_margin, y = pdf.t_margin, w = pdf_width, h = pdf_height)
except FileNotFoundError:
    pdf.multi_cell(0, 10, txt = "Combined visualization image not found.")
except Exception as e:
    pdf.multi_cell(0, 10, txt = f"Error adding image: {e}")

# Add a page for the statistics
pdf.add_page()

# Add the text statistics from the .txt file
stats_file_path = 'drive/MyDrive/p-log/'+ filename + '-stats.txt'
try:
    with open(stats_file_path, 'r') as f:
        stats_text = f.read()
    pdf.multi_cell(0, 10, txt = stats_text)
except FileNotFoundError:
    pdf.multi_cell(0, 10, txt = "Statistics file not found.")


# Save the PDF
pdf.output(output_pdf_path)

print(f"\nReport exported to PDF: {output_pdf_path}")
