from pandas import *

# https://www.futurelearn.com/courses/learn-to-code/7/steps/395833
LOCATION='comtrade_milk_uk_monthly_14.csv'

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
milk = read_csv(LOCATION, dtype={'Commodity Code':str, 'Reporter Code':str})

print("\n             Comtrade\n%s.\n" % milk.head(3))
# Limit the columns to make the dataframe easier to work with by selecting
# just a subset of them.

COLUMNS = ['Year', 'Period','Trade Flow','Reporter', 'Partner', 'Commodity',
           'Commodity Code','Trade Value (US$)']
milk = milk[COLUMNS]

# Derive two new dataframes that separate out the 'World' partner data
# and the data for individual partner countries.
milk_world = milk[milk['Partner'] == 'World']
milk_countries = milk[milk['Partner'] != 'World']
#Store a local copy as a CSV file
milk_countries.to_csv('countrymilk.csv', index=False)
#Load the  data
load_test = read_csv('countrymilk.csv', dtype={'Commodity Code':str, 'Reporter Code':str})
# Another way
#load_test=read_csv('countrymilk.csv', dtype={'Commodity Code':str}, encoding = "ISO-8859-1")
print("\ncountrymilk.csv\n%s.\n" % load_test.head(2))


# For large or heterogenous datasets, it is often convenient to
# create subsets of the data. To further separate out the imports:

milk_imports = milk[    milk['Trade Flow'] == 'Imports'   ]

milk_countries_imports = milk_countries[  milk_countries['Trade Flow'] == 'Imports']

milk_world_imports = milk_world[   milk_world['Trade Flow'] == 'Imports' ]

#Sorting the data
# Having loaded in the data, find the most valuable partners in terms of
# import trade flow during a particular month by sorting the data by
#  decreasing trade value and then selecting the top few rows.

milkImportsInJanuary2014 =\
      milk_countries_imports[milk_countries_imports['Period'] == 201401]

milk_ci = milkImportsInJanuary2014.sort_values('Trade Value (US$)',ascending=False).head(10)
print("\nMilk Imports In January 2014\n%s\n" % milk_ci)

# Exercise 2: Grouping data