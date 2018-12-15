from pandas import *

# https://www.futurelearn.com/courses/learn-to-code/7/steps/395833
LOCATION = 'comtrade_milk_uk_monthly_14.csv'

'''
The data is obtained from the United Nations Comtrade: 
     comtrade.un.org/data/,
 by selecting the following configuration:
    Type of Product: goods
    Frequency: monthly
    Periods: all of 2014
    Reporter: United Kingdom
    Partners: all
    Flows: imports and exports
    HS (as reported) commodity codes: 
            0401 (Milk and cream, neither concentrated nor sweetened)
            0402 (Milk and    cream, concentrated or sweetened)
Clicking on 'Preview' results in a message that the data exceeds 500 rows.
 Data was downloaded using the Download CSV button and the download file 
 renamed appropriately.
'''

# Load the data in from the specified location, ensuring that the various codes
# are read as strings.
milk = read_csv(LOCATION, dtype={'Commodity Code': str, 'Reporter Code': str})

print("\n             Comtrade\n%s.\n" % milk.head(3))
# Limit the columns to make the dataframe easier to work with by selecting
# just a subset of them.

COLUMNS = ['Year', 'Period', 'Trade Flow', 'Reporter', 'Partner', 'Commodity',
           'Commodity Code', 'Trade Value (US$)']
milk = milk[COLUMNS]

# Derive two new dataframes that separate out the 'World' partner data
# and the data for individual partner countries.
milk_world = milk[milk['Partner'] == 'World']
milk_countries = milk[milk['Partner'] != 'World']
# Store a local copy as a CSV file
milk_countries.to_csv('countrymilk.csv', index=False)
# Load the  data
load_test = read_csv('countrymilk.csv', dtype={'Commodity Code': str, 'Reporter Code': str})
# Another way
# load_test=read_csv('countrymilk.csv', dtype={'Commodity Code':str}, encoding = "ISO-8859-1")
print("\ncountrymilk.csv\n%s.\n" % load_test.head(2))

# For large or heterogenous datasets, it is often convenient to
# create subsets of the data. To further separate out the imports:

milk_imports = milk[milk['Trade Flow'] == 'Imports']

milk_countries_imports = milk_countries[milk_countries['Trade Flow'] == 'Imports']

milk_world_imports = milk_world[milk_world['Trade Flow'] == 'Imports']

# Sorting the data
# Having loaded in the data, find the most valuable partners in terms of
# import trade flow during a particular month by sorting the data by
#  decreasing trade value and then selecting the top few rows.

milkImportsInJanuary2014 = \
    milk_countries_imports[milk_countries_imports['Period'] == 201401]
# Sorting the data
milk_ci = milkImportsInJanuary2014.sort_values('Trade Value (US$)', ascending=False).head(10)

milkImportsInJanuary2014.sort_values('Trade Value (US$)', ascending=False).head(5)
print("\nMilk Imports In January 2014\n%s\n" % milk_ci)

# Grouping data = process whereby rows associated with a particular group
# are collated so that you can work with just those rows
#  as distinct subsets of the whole dataset.

# The groupby() method runs down each row in a data frame, splitting the rows
# into separate groups
# based on the unique values associated with the key column or columns.

# Split the data into two different subsets of data
# (imports and exports), by grouping on trade flow.

groups = milk_countries.groupby('Trade Flow')# imports and exports
groups.get_group('Imports').head()
print("\n Reporter: United Kingdom Group By  Imports:\n%s\n" % groups.get_group('Imports').head())
#groups based on commodity code and trade flow
GROUPING_COMMFLOW = ['Commodity Code','Trade Flow']

groups = milk_countries.groupby(GROUPING_COMMFLOW)
print("\n groups.groups.keys():\n%s\n" %  groups.groups.keys())
'''
The  output:
dict_keys([('0401', 'Exports'), ('0401', 'Imports'),
 ('0402', 'Exports'), ('0402', 'Imports')])
 for every product two  type of 'Trade Flow'
'''
'''
If a grouping is based on the 'Partner' and 
'Trade Flow' columns, the argument of get_group has to be
 a partner/flow pair, like ('France', 'Import') to get 
 all rows associated with imports from France.
'''

GROUPING_PARTNERFLOW = ['Partner','Trade Flow']
groups = milk_countries.groupby(GROUPING_PARTNERFLOW)
GROUP_PARTNERFLOW= ('France','Imports')

print("\ngroups.get_group( GROUP_PARTNERFLOW ):\n%s\n" %groups.get_group( GROUP_PARTNERFLOW ))
#To find the leading partner for a particular commodity, group by commodity,
#  get the desired group, and then sort the result.
groups = milk_countries.groupby(['Commodity Code'])
so = groups.get_group('0402').sort_values("Trade Value (US$)", ascending=False).head(2)
print("\nleading partner groups.get_group('0402'):\n\n", so)

'''
Exercise 3: Experimenting with Split-Apply-Combine – Summary reports
Aggegration operations can be invoked using the aggregate() method.
to find the total value of imports traded for each commodity within
 the period, take the world dataframe, and sum the values over the 
 trade value column within each grouping.
'''
#milk_world_imports = milk_world[milk_world['Trade Flow'] == 'Imports']
c = milk_world_imports.groupby('Commodity Code')['Period','Trade Value (US$)']
print("\n  Trade Value:\n\n", c.head(11) )

c = milk_world_imports.groupby('Commodity Code')['Trade Value (US$)'].aggregate(sum)
print("\n  1:aggregate(sum):\n\n", c )
#So that's 222 million dollars or so on the 0401 commodity, and 341 million dollars or so on 0402.

#If you total (sum) up all the individual country contributions,
#you should get similar amounts.
milk_imports_grouped=milk_countries_imports.groupby('Commodity Code')
c = milk_imports_grouped['Trade Value (US$)'].aggregate(sum)
print("\n  2:aggregate(sum):\n\n", c )

# Finding top ranked elements within a group
milk_countries_imports_totals = \
    milk_countries_imports.groupby('Partner')[['Trade Value (US$)']].aggregate(sum)
c = milk_countries_imports_totals.sort_values('Trade Value (US$)', ascending=False).head()
print("\n  milk_countries_imports_totals.sort_values :\n\n", c )

'''
Generating simple charts
One of the useful features of the aggregate() method is that it 
returns an object that can be plotted from directly, in 
this example a horizontal bar chart.
'''
import matplotlib.pyplot as plt
milk_imports_grouped['Trade Value (US$)'].aggregate(sum).plot(kind='barh')
plt.show()

'''
Generating alternative groupings
Reports can also be generated to show the total imports per month 
for each commodity: group on commodity, trade flow and period,
 and then sum the trade values contained within each group.
'''
monthlies = milk_countries_imports.groupby(['Commodity','Trade Flow','Period'])['Trade Value (US$)'].aggregate(sum)
print("\n *********     monthlies :\n\n", monthlies)

'''
 Generating several aggregation values at the same time

To generate several aggregate reports in a single line of code, provide 
a list of several aggregating  operations to the aggregate() method:
'''
from numpy import mean

GROUPING_COMMFLOWPERIOD=['Commodity','Trade Flow','Period']
c = milk_countries.groupby(GROUPING_COMMFLOWPERIOD)['Trade Value (US$)'].aggregate([sum, min, max, mean])
print("\n several aggregate reports +++:\n\n", monthlies)

#For example, plot the maximum value by month across each code/period
# combination to
# see which month saw the maximum peak flow of imports from a single partner.
milk_countries_imports.groupby(['Commodity Code','Period'])['Trade Value (US$)'].aggregate(max).plot(kind='barh')
plt.show()

# Exercise 4: Filtering groups

'''
If you have a large dataset that can be split into multiple groups 
but for which you only want to report on groups that have a particular 
property, the filter() method can be used to apply a test to a group and 
only return rows from groups that pass a particular group-wide test. 
If the test evaluates as False, the rows included in that group will be ignored.
'''
# Df is a new  dataframe
df = DataFrame({'Commodity' : ['Fish', 'Milk', 'Eggs', 'Fish', 'Milk'],
                'Trade Flow' : ['Import', 'Import', 'Import', 'Export','Export'],
                'Value' : [1,2,4,8,16]})

print("\n filter():\n\n", df)

# In the following case, group by trade flow and only return rows
# from groups containing three or more rows.
def groupsOfThreeOrMoreRows(g):
    print("\n groupsOfThreeOrMoreRows :\n\n",g)
    return len(g) >= 3

c = df.groupby('Trade Flow').filter(groupsOfThreeOrMoreRows)

print("\n filter  3:\n\n", c )

#Select just those commodities where the sum of import and export values
# is greater than a certain amount to indicate which ones have a large
# value of trade, in whatever direction,
# associated with them.
#  First group by the commodity, then filter on the group property of interest.

def groupsWithValueGreaterThanFive(g):
    return g['Value'].sum() > 5

c = df.groupby('Commodity').filter(groupsWithValueGreaterThanFive)

print("\n filter  5:\n\n", c )