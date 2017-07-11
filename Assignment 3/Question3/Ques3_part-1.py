
# coding: utf-8

# In[89]:

#import pandas and read csv
import pandas as pd
import numpy as np

dfCricket = pd.read_csv("cricket_matches.csv")


# In[90]:

#Get records where team which host the game and win the game.
dfCricket_1=dfCricket[dfCricket['home']==dfCricket['winner']]


# In[91]:

#Get the runs scored in that innings for winning team
dfCricket_1['Scores'] = np.where(dfCricket_1['winner'] == dfCricket_1['innings1'],dfCricket_1['innings1_runs'],dfCricket_1['innings2_runs'] )


# In[103]:

#Get mean value of winning scores
df = dfCricket_1.groupby('home', as_index=False)['Scores'].mean()
print(df.head())


# In[104]:

#Write to CSV file
df.to_csv('Q3_part1.csv')

