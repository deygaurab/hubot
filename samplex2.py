import xlrd
import json

workbook = xlrd.open_workbook('runbook.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')
num_rows = worksheet.nrows - 1
num_cells = worksheet.ncols - 1

# Fetch all the column names from first row
colnames = []
for i in range(num_cells + 1):
    colnames.append(worksheet.cell_value(0, i))
print(colnames)
print(len(colnames))
curr_row = 0

result = {}

with open('runbook.json', 'a') as fr:
    while curr_row < num_rows:
        curr_row += 1
        index_json = json.dumps({"index": {"_id": curr_row}})
        fr.write(index_json)
        fr.write("\n")
        row = worksheet.row(curr_row)
        # print('Row:', curr_row)
        curr_cell = -1
        data = {}
        while curr_cell < num_cells:
            curr_cell += 1
            # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
            cell_type = worksheet.cell_type(curr_row, curr_cell)
            cell_value = worksheet.cell_value(curr_row, curr_cell)
            data[colnames[curr_cell]] = cell_value
            # print(' ', cell_type, ':', cell_value)
        result[curr_row] = data
        fr.write(json.dumps(data))
        fr.write("\n")

# with open('file1.json', 'w') as fw:
#     json.dump(result, fw)
