# pdf generator.
from fpdf import FPDF

# create the instance
pdf = FPDF(orientation='P', unit='mm', format='A4')

# adding a page
pdf.add_page()

# font for page

pdf.set_font('Arial', 'B', size=12)

# creating a cell
pdf.cell(0, 12, txt='Hello World!', ln=1, align='l')

pdf.output('test.pdf')