from openpyxl import load_workbook

#load work book
wb = load_workbook(filename = 'Data.xlsx')

#load Sheet1
sheet_ranges = wb['Sheet1']

print("Value of cell A2 before change: " + sheet_ranges['A2'].value)

sheet_ranges['A2'].value = 'John'

print("Value of cell A2 After change: " + sheet_ranges['A2'].value)

wb.save('Data.xlsx')