
import xlwt  #faila iezveidei un rediģēšana
import xlrd # faila nolasīšana


darbaGramata = xlrd.open_Workbook('Excel_piemers.xls')
lapa = darbaGramata.sheet_by_index(0)

for rinda in lapa:
    print(rinda)



