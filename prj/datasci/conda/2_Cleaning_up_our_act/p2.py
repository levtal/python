from pandas import *
# Exercise notebook 2 https://cocalc.com/projects/
df = read_csv('WHO POP TB all.csv')
col = df.columns#columns holds a dataframe's column names.
print("column names = %r" % col)
# `iloc` attribute can be used to obtain the row at the given index.
print("first row, index 0 :")
print(df.iloc[0])
print("third row, index 2 :")
print(df.iloc[2])
print("first five rows :")
print(df.head()) # first five rows
print("first 7 rows :")
print(df.head(7)) # first 7 rows
print(df.tail(7)) # last 7 rows

col_list = ['Country', 'Population (1000s)']
cu_po = df[col_list].head(7)
print(cu_po)# Print 7 rows of the above columns


print("Third value of deaths column = %r" % df['TB deaths'].iloc[2])


# display the first eight rows from the 'Country' and 'TB deaths' columns.'
col_list = ['Country', 'TB deaths']
co_de = df[col_list].head(8)
print(co_de)
# countries where the Population (1000s) is less than or equal to 50000 or
#  TB deaths are greater  than or equal to 20000


print('Countries:Population (1000s) <= 50000 or TB deaths > 20000')
r = (df['Population (1000s)'] > 5000) & (df['TB deaths'] > 20000)
# r Contains only  true and false
print(df[r])#  df[r] is a new data frame.   Only the True reault is printed
r = (df['Country'] >= 'Suriname') & (df['Country'] <= 'Togo')
print(df[r])