from xlwt import Workbook

def write_headers_to_excel(dataSheet,argList):
        row = 0
        col = 0
        for colHeader in argList:
                dataSheet.write(row, col, colHeader)
                col+=1
    
def write_data_to_excel(dataSheet,argList):
        row = 1
        for eachRow in argList:
                col = 0
                for cellValue in eachRow:
                        dataSheet.write(row, col, cellValue)
                        col += 1 
                row += 1

def generate_Excel(fileName,tabName,oneDimensionalHeaderList,twoDimensionalDataList):
        wb = Workbook()
        dataSheet = wb.add_sheet(tabName,cell_overwrite_ok=True)
        write_headers_to_excel(dataSheet,oneDimensionalHeaderList)
        write_data_to_excel(dataSheet,twoDimensionalDataList)
        wb.save(fileName)