
# coding: utf-8

# In[19]:

#import pandas and read csv
import pandas as pd
dfNYC = pd.read_csv("vehicle_collisions.csv")


# In[20]:

#Count collisions for every type
dfNYC['No_of_collisions'] = dfNYC[['VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE']].apply(lambda x: x.count(), axis=1)


# In[21]:

#Group by borough & no of collisions
dfCollisions = dfNYC.groupby(['BOROUGH','No_of_collisions']).size().unstack()

#Calculate the More than 4 vehicles column
dfCollisions['More_vehicle_involved'] = dfCollisions[0] + dfCollisions[4] + dfCollisions[5]
dfCollisions = dfCollisions.drop([0,4,5], axis=1)

#Rename the columns
dfCollisions.columns = ['One_vehicle_involved', 'Two_vehicle_involved','Three_vehicle_involved','More_vehicle_involved']
print(dfCollisions.head())


# In[22]:

#Write to CSV file
dfCollisions.to_csv('Q1_part2.csv')

