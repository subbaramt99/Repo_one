import pandas as pd
from openpyxl import load_workbook

file_path = 'Downloads/2nd Jan 2025 Dashboard-1.xlsx'
df = pd.read_excel(file_path)
print(df.head()) # it will read the excel file of 1st sheet


df1 = pd.read_excel("test.xlsx", sheet_name= "sheet2")
print(df.head()) # it will read the excel file of specfic sheet

df2 = pd.read_excel("test.xlsx", usecols= ["column1", "column1"])
print(df.head()) # it will read the excel file of specfic sheet


#*********************Using openpyxl ***************************************

#load workbook
wb = load_workbook("test.xlsx")
sheet = wb["sheet1"]

print(sheet["A"].value)
#Iterate through rows
for row in sheet.iter_row(values_only = True):
    print(row)
