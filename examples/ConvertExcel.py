from netcell import convert_excel_to_netcell

# Converts 'financial_data.xlsx' to 'financial_data.ncell'
# Each tab in Excel becomes a searchable sheet in NetCell
convert_excel_to_netcell("financial_data.xlsx")

# Immediately query the new file
import netcell
db = netcell.open("financial_data.ncell")
print("Sheets found:", db.list_sheets())