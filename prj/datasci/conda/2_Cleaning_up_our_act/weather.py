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
# elect the rows where the direction is greater than or equal to 350
# or smaller than or equal to 10
wind_deg = london['WindDirDegrees']
start = 350
end = 10
north = london[(wind_deg >= start) | (wind_deg <= end)]
print()
print('direction is >= 350 or <= to 10')
print(north)



# Changing the data type of the 'GMT' column
# convert a column of object (string) values such as those in the
# 'GMT' column into values of a proper  date type called datetime64
london['GMT'] = to_datetime(london['GMT'])
# Display the types of all the columns again so we
# can check the changes have been made.
print(london.dtypes)

# Return the row where the date is 4 June 2014
print()
print("Rows where the date is 4 June 2014")
'''
‘2014-1-3’ is a string and the values in the 
‘GMT’ column are of type datetime64.  So we
create a datetime64 value using the datetime() function like this:
datetime(2014, 6, 4)
'''
dat = datetime(2014, 6, 4)
print(london[london['GMT'] == dat])
# Return all the rows where the    date is between 8 December 2014
# and 12 December 2014’
print (london[(london['GMT'] >= datetime(2014, 12, 8))
& (london['GMT'] <= datetime(2014, 12, 12))])

# Changing column 'GMT'  index to datetime64 values
london.index = london['GMT']
#Display the first 2 rows
print(london.head(2))
print('Get  the [2014, 1, 1]row using the dataframe’s ix (index) ')
print(london.ix[datetime(2014, 1, 1)])
print()
print('Rows where the date is between 8 December and 12 December')
print(london.ix[datetime(2014,12,8) :  datetime(2014,12,12)])
print()
londonSpring = london.loc[datetime(2014,3,1) : datetime(2014,5,31)]
londonSpring['Mean Humidity'].plot(grid=True, figsize=(10,5))
print()