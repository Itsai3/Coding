import os
from datetime import date
from pprint import pprint


from simple_smartsheet import Smartsheet
from simple_smartsheet.models import Sheet, Column, Row, Cell, ColumnType

# API Access Code for "ClarityTest": GvMhxd667tXV7duI5gGjOEcXG47kLGYJaoc3A

TOKEN = 'GvMhxd667tXV7duI5gGjOEcXG47kLGYJaoc3A'
smartsheet = Smartsheet(TOKEN)

SHEET_NAME = "ClarityTest"
sheet = smartsheet.sheets.get(SHEET_NAME)

print(sheet)
# sheet = smartsheet.sheets.sort_rows(
#     sheet, [{"column_title": "Full Name", "descending": True}]
# )

print("\nSheet after adding rows:")

# print("\nSheet after adding rows:")
# print a list of dictionaries containing column titles and values for each row
# pprint(sheet.as_list())