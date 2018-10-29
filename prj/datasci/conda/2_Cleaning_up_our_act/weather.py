from pandas import *
# https://www.futurelearn.com/courses/learn-to-code/7/steps/395803
#london = read_csv('London_2014.csv')
london = read_csv('London_2014.csv', skipinitialspace=True)
#print(london.head())
print("Column names for the dataframe")
print(london.columns)
col_list = ['Mean Humidity', 'CloudCover', 'Events']
print(col_list)
print(london[col_list].head(2))
# This is a list ['Mean Humidity', 'CloudCover', 'Events']
print('first row of data in the dataframe ')
print(london.iloc[2])  # New version of london.irow(2)
# The last column name is  'WindDirDegrees< br />'.
# WE need to  change it to   'WindDirDegrees'
# So we call rename() method as follows:
london = london.rename(columns={'WindDirDegrees<br />':'WindDirDegrees'})
print("Column names for the dataframe after calling rename()")
print(london.columns)
print(london[['WindDirDegrees']].head(2))
# We need  to remove </br> string from  actul data using  str.rstrip('<br />'
london['WindDirDegrees'] = london['WindDirDegrees'].str.rstrip('<br />')

# Let’s display the first few rows of the 'WindDirDegrees' to confirm the changes:
print("after str.rstrip('<br />'")
print(london[['WindDirDegrees']].head(2))

# Finding missing values in 'Events' column
print(london['Events'].isnull())

# new dataframe consisting of all the rows without
#  recorded events (rain, fog, thunderstorm, etc.)
print()
print("all the rows without  recorded events")
print(london[london['Events'].isnull()])
print()
print("num of missing observations")
print(london.isnull().sum()) #num of missing observations
# fillna() will replace all non-available values with the value given as argument.
london['Events'] = london['Events'].fillna('')
print(london[london['Events'].isnull()])# This will print empty  dataframe
print(london.dtypes)# dataframe’s dtypes attribute
#  Changing the data type of the 'WindDirDegrees' column

# The read_csv() method has interpreted the values in the
# 'WindDirDegrees' column as strings (type object)
# The values in the 'WindDirDegrees' column are
# meant to represent wind direction in terms of
# degrees from true north (360)
# To do this we need to change the data type of the ‘WindDirDegrees’
# column from object to type int64.
# We can do that by using the astype()
london['WindDirDegrees'] = london['WindDirDegrees'].astype('int64')
print('Rows where the wind direction is greater than 350 degrees’')
print(london[london['WindDirDegrees'] > 350])

#Changing the data type of the 'GMT' column
