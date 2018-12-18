<<<<<<< HEAD
from pandas import *
import pandas as pd
# https://www.futurelearn.com/courses/learn-to-code/7/steps/395822
#https://data.worldbank.org/
#http://data.worldbank.org/indicator/NY.GDP.MKTP.CD

def roundToMillions(value):
    result = round(value / 1000000)
    return result


# converts US dollars to British pounds.
def usdToGBP(usd):
    return usd / 1.564768  # average rate during 2013

data = read_csv('WB GDP 2013.csv')
lifeReset = read_csv('WB LE 2013.csv')
popReset = read_csv('WB POP 2013.csv')
YEAR = 2013
GDP_INDICATOR = 'NY.GDP.MKTP.CD'
LIFE_INDICATOR = 'SP.DYN.LE00.IN'
POP_INDICATOR ='SP.POP.TOTL'
gdpReset = data
print("\n             GDP\n%s.\n" % gdpReset.head())
print("\n             life\n%s.\n" % lifeReset.head())

'''
The initial rows are not about countries, 
but groups of countries. 
Such aggregated values need to be removed, because we’re only 
interested in individual countries.
'''
print("\n GDP line 0 to 2\n%s.\n" % gdpReset[0:3])

print("\n gdp[240:]\n%s.\n" % gdpReset[240:])

'''The first 34 rows of World Bank dataframes 
are aggregated data for country groups, and are thus discarded.
  '''
gdpCountries = gdpReset[34:]
lifeCountries = lifeReset[34:]
#Rows with missing data are dropped.
gdpData = gdpCountries.dropna()
lifeData = lifeCountries.dropna()
gdpData.head()

# drop the irrelevant year column.
COUNTRY = 'country'
headings = [COUNTRY, GDP_INDICATOR]
gdpClean = gdpData[headings]
headings = [COUNTRY, LIFE_INDICATOR]
lifeClean = lifeData[headings]


#Exercise 9: Joining and transforming
#https://www.futurelearn.com/courses/learn-to-code/7/steps/395825
#The two dataframes can now be merged with an inner join.
gdpVsLifeAll = merge(gdpClean, lifeClean, on=COUNTRY, how='inner')


print("\n Merged two dataframes  \n%s.\n" % gdpVsLifeAll.head())

# The dollars are converted to million pounds.
GDP = 'GDP (£m)'
column = gdpVsLifeAll[GDP_INDICATOR]
gdpVsLifeAll[GDP] = column.apply(usdToGBP).apply(roundToMillions)
print("\nThe dollars are converted to million pounds.  \n%s\n" % gdpVsLifeAll.head())
# The life expectancy is rounded, by applying the round() function
LIFE = 'Life expectancy (years)'
gdpVsLifeAll[LIFE] = gdpVsLifeAll[LIFE_INDICATOR].apply(round)


LIFE = 'Life expectancy (years)'
gdpVsLifeAll[LIFE] = gdpVsLifeAll[LIFE_INDICATOR].apply(round)

print("\nThe life expectancy is rounded.  \n%s\n" % gdpVsLifeAll.head())
#The original GDP and life expectancy columns are dropped.
headings = [COUNTRY, GDP, LIFE]
gdpVsLifeClean = gdpVsLifeAll[headings]

print("\nOriginal GDP and life expectancy columns are dropped.  \n%s\n" % gdpVsLifeClean.head())


'''
Exercise 10: Correlation
The Spearman rank correlation coefficient between GDP and life expectancy,
 and the corresponding p-value are calculated as follows.
'''
from scipy.stats import spearmanr

gdpColumn = gdpVsLifeClean[GDP]
lifeColumn = gdpVsLifeClean[LIFE]

(correlation, pValue) = spearmanr(gdpColumn, lifeColumn)
print('The correlation is', correlation)
if pValue < 0.05:
    print('It is statistically significant.')
else:
    print('It is not statistically significant.')
#Exercise 10.
#Calculate the correlation
#between GDP and population in Exercise 10 in the Week 3 Exercise notebook.
POP_INDICATOR ='SP.POP.TOTL'

popReset = read_csv('WB POP 2013.csv')
print("\n             Population\n%s.\n" % popReset.head())
popCountries = popReset[34:]
popData = popCountries.dropna()
headings = [COUNTRY, POP_INDICATOR]
popClean = popData[headings]


import matplotlib.pyplot as plt
gdpVsLifeAll.plot(x=GDP, y=LIFE, kind='scatter', grid=True)


gdpVsLifeAll.plot(x=GDP, y=LIFE, kind='scatter', grid=True,
	       logx=True, figsize = (10, 4))
plt.show()
=======
from pandas import *
import pandas as pd
# https://www.futurelearn.com/courses/learn-to-code/7/steps/395822
#https://data.worldbank.org/
#http://data.worldbank.org/indicator/NY.GDP.MKTP.CD

def roundToMillions(value):
    result = round(value / 1000000)
    return result


# converts US dollars to British pounds.
def usdToGBP(usd):
    return usd / 1.564768  # average rate during 2013

data = read_csv('WB GDP 2013.csv')
lifeReset = read_csv('WB LE 2013.csv')
popReset = read_csv('WB POP 2013.csv')
YEAR = 2013
GDP_INDICATOR = 'NY.GDP.MKTP.CD'
LIFE_INDICATOR = 'SP.DYN.LE00.IN'
POP_INDICATOR ='SP.POP.TOTL'
gdpReset = data
print("\n             GDP\n%s.\n" % gdpReset.head())
print("\n             life\n%s.\n" % lifeReset.head())

'''
The initial rows are not about countries, 
but groups of countries. 
Such aggregated values need to be removed, because we’re only 
interested in individual countries.
'''
print("\n GDP line 0 to 2\n%s.\n" % gdpReset[0:3])

print("\n gdp[240:]\n%s.\n" % gdpReset[240:])

'''The first 34 rows of World Bank dataframes 
are aggregated data for country groups, and are thus discarded.
  '''
gdpCountries = gdpReset[34:]
lifeCountries = lifeReset[34:]
#Rows with missing data are dropped.
gdpData = gdpCountries.dropna()
lifeData = lifeCountries.dropna()
gdpData.head()

# drop the irrelevant year column.
COUNTRY = 'country'
headings = [COUNTRY, GDP_INDICATOR]
gdpClean = gdpData[headings]
headings = [COUNTRY, LIFE_INDICATOR]
lifeClean = lifeData[headings]


#Exercise 9: Joining and transforming
#https://www.futurelearn.com/courses/learn-to-code/7/steps/395825
#The two dataframes can now be merged with an inner join.
gdpVsLifeAll = merge(gdpClean, lifeClean, on=COUNTRY, how='inner')


print("\n Merged two dataframes  \n%s.\n" % gdpVsLifeAll.head())

# The dollars are converted to million pounds.
GDP = 'GDP (£m)'
column = gdpVsLifeAll[GDP_INDICATOR]
gdpVsLifeAll[GDP] = column.apply(usdToGBP).apply(roundToMillions)
print("\nThe dollars are converted to million pounds.  \n%s\n" % gdpVsLifeAll.head())
# The life expectancy is rounded, by applying the round() function
LIFE = 'Life expectancy (years)'
gdpVsLifeAll[LIFE] = gdpVsLifeAll[LIFE_INDICATOR].apply(round)


LIFE = 'Life expectancy (years)'
gdpVsLifeAll[LIFE] = gdpVsLifeAll[LIFE_INDICATOR].apply(round)

print("\nThe life expectancy is rounded.  \n%s\n" % gdpVsLifeAll.head())
#The original GDP and life expectancy columns are dropped.
headings = [COUNTRY, GDP, LIFE]
gdpVsLifeClean = gdpVsLifeAll[headings]

print("\nOriginal GDP and life expectancy columns are dropped.  \n%s\n" % gdpVsLifeClean.head())


'''
Exercise 10: Correlation

The Spearman rank correlation coefficient between GDP and life expectancy,
 and the corresponding p-value are calculated as follows.

'''
from scipy.stats import spearmanr

gdpColumn = gdpVsLifeClean[GDP]
lifeColumn = gdpVsLifeClean[LIFE]

(correlation, pValue) = spearmanr(gdpColumn, lifeColumn)
print('The correlation is', correlation)
if pValue < 0.05:
    print('It is statistically significant.')
else:
    print('It is not statistically significant.')
#Exercise 10.
#Calculate the correlation
#between GDP and population in Exercise 10 in the Week 3 Exercise notebook.
POP_INDICATOR ='SP.POP.TOTL'

popReset = read_csv('WB POP 2013.csv')
print("\n             Population\n%s.\n" % popReset.head())
popCountries = popReset[34:]
popData = popCountries.dropna()
headings = [COUNTRY, POP_INDICATOR]
popClean = popData[headings]


import matplotlib.pyplot as plt
gdpVsLifeAll.plot(x=GDP, y=LIFE, kind='scatter', grid=True)


gdpVsLifeAll.plot(x=GDP, y=LIFE, kind='scatter', grid=True,
	       logx=True, figsize = (10, 4))
plt.show()
>>>>>>> 6c8bdb10278692f8cb3a7f145d07605ced8b35f8
print("\n             Population\n%s.\n" % popClean.head())