# pdf generator.
from fpdf import FPDF

# create the instance
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

