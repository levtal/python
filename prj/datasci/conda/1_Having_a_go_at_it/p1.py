#!/usr/bin/env python
from pandas import *
data = read_excel('WHO POP TB some.xls')
print(data)
tbColumn = data['TB deaths']
print(tbColumn)