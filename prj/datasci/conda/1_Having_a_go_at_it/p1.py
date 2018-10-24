#!/usr/bin/env python
# This is the python 3.2 of the"Exercise1.ipyntab" jupiter
from pandas import *
data = read_excel('WHO POP TB some.xls')

print("         File:WHO POP TB some.xls" )
print(data)
tbColumn = data['TB deaths']
print("         Column:TB deaths")
print(tbColumn)

tbColumn = data['TB deaths']
print("TB deaths(sum) = %r" % tbColumn.sum())
print("TB deaths(min) = %r" % tbColumn.min())
print("TB deaths(mean) = %r" % tbColumn.mean())
print("TB deaths(median) = %r" % tbColumn.median())
print("TB deaths(sort_values)")
print(data.sort_values('TB deaths'))
print()
print("Death rate of each country")
deathsColumn = data['TB deaths']
populationColumn = data['Population (1000s)']
rateColumn = deathsColumn * 100 / populationColumn
print(rateColumn)
print("Add the new column 'rate' into the dataframe")
data['rate'] = rateColumn
print(data)

