import xlsxwriter

def writeToExcelFile(sheets):
    workbook = xlsxwriter.Workbook('tradeHistory.xlsx')

    for sheet in sheets:
        worksheet = workbook.add_worksheet(sheet["name"])

        data = sheet["data"]
        if(len(data)>0):
            y = 0
            for k in data[0]:
                worksheet.write(0, y, k)
                y = y + 1

        for i in range(len(data)):
            y = 0
            for k in data[i]:
                worksheet.write(i+1, y, data[i][k])
                y = y + 1

    workbook.close()