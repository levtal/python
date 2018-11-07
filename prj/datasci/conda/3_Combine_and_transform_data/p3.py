from pandas import *
# https://www.futurelearn.com/courses/learn-to-code/7/steps/395816
table = [
   ['UK', 2678454886796.7],    # 1st row
   ['USA', 16768100000000.0],  # 2nd row
   ['China', 9240270452047.0], # and so on...
   ['Brazil', 2245673032353.8],
   ['South Africa', 366057913367.1]
]
#To create a dataframe
# Use a pandas function  called DataFrame().
# I have to give it two arguments: the names of the columns and the data
# itself.
# The column names are given as a list of strings,
# the first string being the first column name, etc.

headings = ['Country', 'GDP (US$)']
gdp = DataFrame(columns=headings, data=table)
print(gdp)
print("\n2013 GDP of some countries, in US dollars\n ", gdp)
# define a similar table for the life expectancy,
#  based on the 2013 World Bank data.

headings = ['Country name', 'Life expectancy (years)']
table = [
   ['China', 75],
   ['Russia', 71],
   ['United States', 79],
   ['India', 66],
   ['United Kingdom', 81]
]
life = DataFrame(columns=headings, data=table)
print("\nlife expectancy\n ", life)

# Exercise 2: Defining functions


def roundToMillions(value):
    result = round(value / 1000000)
    return result


print('\n Test function [roundToMillions]==>',roundToMillions(4567890.1) == 5)

# converts US dollars to British pounds.
def usdToGBP(usd):
   return usd / 1.564768  # average rate during 2013

print(usdToGBP(1.564768) == 1)


def expandCountry(name):
   if name == 'UK':  # if the name is 'UK'
      return 'United Kingdom'
   elif name == 'USA':  # otherwise if the name is 'USA'
      return 'United States'
   else:  # otherwise
      return name


print("\nUK name = %s.\n" % expandCountry('UK'))

column = gdp['Country']
print("\nCountrys\n%s.\n" % column)
''''
apply():  applies a given function to each cell in the column,
 returning a new column, in which each cell is the conversion of
the corresponding original cell:
'''
new_col = column.apply(expandCountry)

print("\nCountrys after conversion\n%s.\n" % new_col)

# Add the new column to the dataframe, using a new column heading:

gdp['Country name'] = column.apply(expandCountry)
print("\nThe new dataframe\n%s.\n" % gdp)


# convert the US dollars to British pounds,
# then round to the nearest million, and store the result in a new column
column = gdp['GDP (US$)']
result = column.apply(usdToGBP).apply(roundToMillions)
gdp['GDP (£m)'] = result
print("\nThe new dataframe\n%s.\n" % gdp)


# Now it’s just a matter of selecting the
# two new columns, as the original ones are no longer needed.

headings = ['Country name', 'GDP (£m)']
gdp = gdp[headings]
print("\nLast version dataframe\n%s.\n" % gdp)

# Joining left, right and centre
# join the two tables on  בountry name common column, using the merge().
# If I want to include only those countries appearing in the GDP table,
#  I call the merge() function like so:
lmr = merge(gdp, life, on='Country name', how='left')
print("\nleft Merage dataframe\n%s.\n" % lmr)
rmr = merge(gdp, life, on='Country name', how='right')
print("\nright Merage dataframe\n%s.\n" % rmr)

# The third possibility is an outer join which takes all countries,
#  i.e. whether they are in the left or right table. The result has all the rows of the left and right joins:

omr = merge(gdp, life, on='Country name', how='outer')
print("\nouter Merage dataframe\n%s.\n" % omr)

#inner join   takes only those countries common to
# both tables, i.e. for which I know the GDP and the life expectancy.
# That’s the join I want, to avoid any undefined values:



gdpVsLife = merge(gdp, life, on='Country name', how='inner')
print("\niner Merage dataframe\n%s.\n" % gdpVsLife)