import xlsxwriter

def writeToExcelFile(dataset):
    workbook = xlsxwriter.Workbook('tradeHistory.xlsx')

    dataIndex = 0
    for data in dataset:
        dataIndex = dataIndex + 1
        title = str(dataIndex) + " - " + data[0]["type"] + " - " + data[0]["apikey"][:10] + "..."
        worksheet = workbook.add_worksheet(title)

        trades = data[1]
        if(len(trades)>0):
            y = 0
            for k in trades[0]:
                worksheet.write(0, y, k)
                y = y + 1

        for i in range(len(trades)):
            y = 0
            for k in trades[i]:
                worksheet.write(i+1, y, trades[i][k])
                y = y + 1

    workbook.close()