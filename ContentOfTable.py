import xlsxwriter
import os

path = input("plase enter path: ")
path = r'{}'.format(path)

workbook = xlsxwriter.Workbook(path + '\contentOfTable(' + path.split('\\')[-1] + ').xlsx')
worksheet = workbook.add_worksheet()
for root, dirs, files in os.walk(path):
    row = 0
    worksheet.write(row, 0, root)
    for dir in dirs:
        row += 1
        worksheet.write(row, 0, row)
        worksheet.write(row, 1, dir)
    break

workbook.close()
print("Done!!!")
