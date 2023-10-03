#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[18]:


class Parcel:
    
    parcels_by_category = {}
    def __init__(self, parcel_number, parcel_weight, parcel_category):
        self.parcel_number = parcel_number
        self.parcel_weight = parcel_weight
        self.parcel_category = parcel_category
        
        if parcel_category in self.parcels_by_category:
            self.parcels_by_category[parcel_category].append(parcel_number)
        else:
            self.parcels_by_category[parcel_category] = [parcel_number]

    def __str__(self):
        return f"Parcel Number: {self.parcel_number}, Category: {self.parcel_category}"
    
parcel1 = Parcel(23456, 10, "filters")
parcel2 = Parcel(66234, 15, "automobile_parts")
parcel3 = Parcel(98432, 30, "Cargo_container")
parcel4 = Parcel(96355, 20, "filters")
parcel5 = Parcel(53463, 40, "Cargo_container")
parcel6 = Parcel(86643, 35, "automobile_parts")
parcel7 = Parcel(64326, 25, "automobile_parts")
parcel8 = Parcel(87653, 5, "Cargo_container")
parcel9 = Parcel(83722, 50, "filters")
print(Parcel.parcels_by_category)


# In[25]:


df = pd.DataFrame.from_dict(Parcel.parcels_by_category, orient='index').transpose()
df=df.fillna(0)
df


# In[20]:


parcel_csv = df.to_csv('parcel.csv', index = True)


# In[ ]:




