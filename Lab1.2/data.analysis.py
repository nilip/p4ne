from matplotlib import pyplot
from openpyxl import load_workbook
wb=load_workbook('data_analysis_lab.xlsx')
sheet=wb['Data']

sheet['A'][1:], ['C'][1:], ['D'][1:]

def getvalue(x): return x.value
a=list(map(getvalue,sheet['A'][1:]))
c=list(map(getvalue,sheet['C'][1:]))
d=list(map(getvalue,sheet['D'][1:]))
pyplot.plot(a, c, label='Метка')
pyplot.plot(a, d, label='Метка')
pyplot.show()
