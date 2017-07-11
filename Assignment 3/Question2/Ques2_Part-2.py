
# coding: utf-8

# In[20]:

#import pandas and read csv

import pandas as pd
dfEComp = pd.read_csv("employee_compensation.csv")


# In[21]:

#Calculate the people whose overtime salary is greater than 5% of salaries 
greaterOvertime = dfEComp['Overtime'] > 0.05 * dfEComp['Salaries'] 
dfgreaterOvertime = dfEComp[greaterOvertime]


# In[25]:

#Group by Job Family and get mean of Total Benefits' and 'Total Compensation'
dfJobFamMean = dfEComp.groupby(['Job Family'])['Total Benefits','Total Compensation'].mean()


# In[26]:

#Calculate Percent_Total_benefit
dfJobFamMean['Percent_Total_benefit'] = (dfJobFamMean['Total Benefits'] / dfJobFamMean['Total Compensation']) * 100


# In[31]:

#Sort values in descending order for Percent_Total_benefit
dfDescendingOrder = dfJobFamMean.sort_values(['Percent_Total_benefit'], ascending=[False])
print(dfDescendingOrder.head())


# In[32]:

#Write to CSV file
dfDescendingOrder.to_csv('Q2_part2.csv')

