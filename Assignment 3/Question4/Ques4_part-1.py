
# coding: utf-8

# In[150]:

#import pandas and read csv
import pandas as pd
import numpy as np
dfAwards = pd.read_csv("movies_awards.csv")


# In[151]:

#Create dataframe with apprpriate column names
columns = ['Total_Awards_won','Total_Awards_nominated', 'Prime_awards_nominated','Oscar_Awards_nominated','Golden_Globe_Awards_nominated','BAFTA_Awards_nominated', 'Prime_awards_won',
           'Oscar_Awards_won','Golden_Globe_Awards_won','BAFTA_Awards_won']
dfAwards = pd.DataFrame(index=dfAwards['Awards'], columns=columns)
dfAwards.reset_index(level=0, inplace=True)
dfAwards = dfAwards.fillna(0)
dfTotalAwards = dfAwards.drop(dfAwards[dfAwards['Awards'] == 0].index)


# In[152]:

#Use regex and str.extract to get the specific number of wins and nominations for each Award
dfTotalAwards['Prime_awards_nominated'] = dfTotalAwards['Awards'].str.extract("for (\d+) Primetime",expand=True).apply(pd.to_numeric).fillna(0)
dfTotalAwards['Oscar_Awards_nominated'] = dfTotalAwards['Awards'].str.extract("for (\d+) Oscar",expand=True).apply(pd.to_numeric).fillna(0)
dfTotalAwards['Golden_Globe_Awards_nominated'] = dfTotalAwards['Awards'].str.extract("for (\d+) Golden",expand=True).apply(pd.to_numeric).fillna(0)
dfTotalAwards['BAFTA_Awards_nominated'] = dfTotalAwards['Awards'].str.extract("for (\d+) BAFTA",expand=True).apply(pd.to_numeric).fillna(0)
dfTotalAwards['Prime_awards_won'] = dfTotalAwards['Awards'].str.extract("Won (\d+) Primetime",expand=True).apply(pd.to_numeric).fillna(0)
dfTotalAwards['Oscar_Awards_won'] = dfTotalAwards['Awards'].str.extract("Won (\d+) Oscar",expand=True).apply(pd.to_numeric).fillna(0)
dfTotalAwards['Golden_Globe_Awards_won'] = dfTotalAwards['Awards'].str.extract("Won (\d+) Golden",expand=True).apply(pd.to_numeric).fillna(0)
dfTotalAwards['BAFTA_Awards_won'] = dfTotalAwards['Awards'].str.extract("Won (\d+) BAFTA",expand=True).apply(pd.to_numeric).fillna(0)
dfTotalAwards['Awards_won'] = dfTotalAwards['Awards'].str.extract("(\d+) win",expand=True).apply(pd.to_numeric).fillna(0)
dfTotalAwards['Awards_nom'] = dfTotalAwards['Awards'].str.extract("(\d+) nomination",expand=True).apply(pd.to_numeric).fillna(0)



# In[153]:

#Calculate the total awards won and nominated
dfTotalAwards['Total_Awards_won'] = (dfTotalAwards['Awards_won'] + dfTotalAwards['Prime_awards_won'] + dfTotalAwards['Oscar_Awards_won'] + dfTotalAwards['Golden_Globe_Awards_won'] + dfTotalAwards['BAFTA_Awards_won']).apply(pd.to_numeric).fillna(0)
dfTotalAwards['Total_Awards_nominated'] = (dfTotalAwards['Awards_nom'] + dfTotalAwards['Prime_awards_nominated'] + dfTotalAwards['Oscar_Awards_nominated'] + dfTotalAwards['Golden_Globe_Awards_nominated'] + dfTotalAwards['BAFTA_Awards_nominated']).apply(pd.to_numeric).fillna(0)
dfTotalAwards = dfTotalAwards.drop(['Awards_won','Awards_nom'], axis=1)
print(dfTotalAwards.head())



# In[154]:

#Write to CSV file
dfTotalAwards.to_csv('Q4_part1.csv')

