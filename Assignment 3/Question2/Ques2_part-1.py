
# coding: utf-8

# In[38]:

#import pandas and read csv
import pandas as pd
dfEComp = pd.read_csv("employee_compensation.csv")


# In[39]:

#Group by Organization Group & Department and get the mean for Total Compensation
dfMean = dfEComp.groupby(['Organization Group', 'Department'],as_index=False)['Total Compensation'].mean()


# In[40]:

#Sort values in descending order for every department
df = dfMean.groupby(['Organization Group']).apply(lambda s: s.sort_values(['Total Compensation'], ascending=[False])).set_index(['Organization Group', 'Department'])['Total Compensation']
print(df.head())


# In[41]:

#Write to CSV file
df.to_csv('Q2_part1.csv')

