import xlrd

filePath="C://luca//Libro1.xlsx"
openFile= xlrd.open_workbook(filePath)

sheet= openFile.sheet_by_name("Hoja1")


for i in range(  sheet.nrows  ):
    print(sheet.cell_value(i,0), "      ", sheet.cell_value(i,1))


#print ("filas", sheet.nrows)
#print("columnas", sheet.ncols)

