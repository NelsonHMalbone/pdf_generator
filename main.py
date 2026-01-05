# pdf generator.
from fpdf import FPDF
import pandas as pd


# create the instance
pdf = FPDF(orientation='P',
           unit='mm',
           format='A4')
# getting data from csv file
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # adding a page
    pdf.add_page()

    # font for page
    pdf.set_font('Arial',
                 'B',
                 size=12)

    # creating a cell
    pdf.cell(0,
             12,
             txt=row["Topic"],
             ln=1,
             align='l',
             border='B')
pdf.output('test.pdf')