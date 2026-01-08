# pdf generator.
from fpdf import FPDF
import pandas as pd
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

# create the instance
pdf = FPDF(orientation='P',
           unit='mm',
           format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
# getting data from csv file
df = pd.read_csv("topics.csv")

# parent page
for index, row in df.iterrows():
    # adding a page
    pdf.add_page()

    # set for header
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

    #set the footer
    pdf.ln(265)
    pdf.set_font('Arial', style='i', size=10)
    pdf.cell(0, 10, txt=row["Topic"], ln=1, align='R')


    # adding lines to write on
    for y in range(33,285,10):
        pdf.line(10,y,200,y)

    # additional page count
    for x in range(row["Pages"] - 1):
        pdf.add_page()

        # set the footer
        pdf.ln(276)
        pdf.cell(0, 10, txt=row["Topic"], ln=1, align='R')
        pdf.set_font('Arial', style='i', size=10)

        for y in range(10,285,10):
            pdf.line(10,y,200,y)

pdf.output('test.pdf')