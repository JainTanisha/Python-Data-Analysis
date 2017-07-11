
# coding: utf-8

# In[53]:

#Import pandas and read csv

import pandas as pd
dfNYC = pd.read_csv("vehicle_collisions.csv")


# In[54]:

#Convert to str to Date format and get only 2016 data
dfNYC['DATE']=pd.to_datetime(dfNYC['DATE'])
dfNYC16 = dfNYC[dfNYC['DATE'].dt.year==2016]


# In[55]:

#Create dataframe and specific columns
import numpy as np
dfCollisions = pd.DataFrame()
dfCollisions['Month'] = np.arange(1,13)

columns = ['Manhattan','NYC','Percentage']
dfCollisions = pd.DataFrame(index=dfCollisions['Month'], columns=columns).fillna(0)


# In[56]:

#Count collisions for each month in NYC and Manhattan

dfCollisions['NYC'] = dfNYC16['DATE'].groupby([dfNYC16['DATE'].dt.month]).count()
dfMann = dfNYC16[(dfNYC16['BOROUGH'] == 'MANHATTAN')]
dfCollisions['Manhattan'] = dfMann['DATE'].groupby([dfMann['DATE'].dt.month]).count()

#calculate Percentage collisions
dfCollisions['Percentage'] = (dfCollisions['Manhattan'] / dfCollisions['NYC']) * 100


# In[57]:

#Convert Month to Calendar month
dfCollisions.reset_index(level=0, inplace=True)
import calendar
dfCollisions['Month'] = dfCollisions['Month'].apply(lambda x: calendar.month_abbr[x])
print(dfCollisions.head())


# In[50]:

#Write to CSV file
dfCollisions.to_csv('Q1_part1.csv')

