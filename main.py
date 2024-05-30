import glob
import pandas as pd
from fpdf import FPDF

filepaths = glob.glob("invoices/*xlsx")
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet2")
    pdf = FPDF(orientation="p", unit="mm", format="A4")
    pdf.add_page()
    print(df)