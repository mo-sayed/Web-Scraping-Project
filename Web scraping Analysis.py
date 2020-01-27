#!/usr/bin/env python
# coding: utf-8

# # Eataly - Web Scraping Project
# ## by Mohamad Sayed
# 

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


eataly_restaurants = ['New York City', 'Chicago', 'Las Vegas', 'Los Angeles', 'Boston', 'Dallas']
# represents existing locations of eataly in the US\n",
eataly_data = [['New York City', 63799, 8622357, 11084], ['Chicago', 57238, 2670406, 4535],                ['Los Angeles', 62474, 4085014, 3365], ['Boston', 71834, 701984, 5606],                ['Dallas', 52210, 1400337, 1590]]
eataly_df = pd.DataFrame(eataly_data, columns = ['City', 'Median Income', 'Population', 'Density'])


# In[3]:


# path to the directory
# cd Desktop/"NYC DSA"/"lecture slides"/projects/"web scraping"/eataly


# In[4]:


# eataly_df.agg(['std', 'mean'])['Median Income']
# eataly_income_std = eataly_df['Median Income'].agg('std')
eataly_income_std = round(np.std(eataly_df['Median Income']),0)
print('eataly_income_std: ', eataly_income_std)
eataly_income_mean = round(np.mean(eataly_df['Median Income']),0)
print('eataly_income_mean: ', eataly_income_mean)

eataly_population_std = round(np.std(eataly_df['Population']),0)
print('eataly_population_std: ', eataly_population_std)
eataly_population_mean = round(np.mean(eataly_df['Population']),0)
print('eataly_population_mean: ', eataly_population_mean)
eataly_density_std = round(np.std(eataly_df['Density']),0)
print('eataly_density_std: ', eataly_density_std)
eataly_density_mean = round(np.mean(eataly_df['Density']),0)
print('eataly_density_mean: ', eataly_density_mean)


# In[5]:


# yelp_raw_data = pd.read_csv('yelp_reviews.csv', index_col=0)
yelp_raw_data = pd.read_csv('yelp_reviews.csv')
yelp_raw_data


# In[6]:


location_, price_, review_count, reviews_, restaurant_name = [], [], [], [], []


# In[7]:


b = yelp_raw_data.Rating
# string.replace(old, new, count)
b
import re
# b.replace(' star rating', '')
b = yelp_raw_data.Rating.replace(' star rating','', regex=True)
b


# In[8]:


# cleaning up reviews/ratings  
# b = yelp_raw_data.Rating
b = yelp_raw_data.Rating.replace(' star rating','', regex=True)
b
c = list(map(lambda x: x.split(','),b))
c
for i in c:
    for e in i:
        reviews_.append(e)
reviews_


# In[9]:


# cleaning up restaurant names
b = yelp_raw_data.RestName
c = list(map(lambda x: x.split(','),b))
for i in c:
    for e in i:
        restaurant_name.append(e)
restaurant_name


# In[10]:


# cleaning up review counts
b = yelp_raw_data.Nbr_reviews
c = list(map(lambda x: x.split(','),b))
for i in c:
    for e in i:
        review_count.append(e)
review_count


# In[11]:


# cleaning up price
b = yelp_raw_data.Dollar_sign
c = list(map(lambda x: x.split(','),b))
for i in c:
    for e in i:
        price_.append(e)
price_


# In[12]:


# cleaning up city/state data
location_ = [] 
b = yelp_raw_data.City
b_str = ','.join([str(elem) for elem in b])
b_str

b_split = b_str.split(',')
location_ = [",".join(b_split[i:i+2]) for i in range(0, len(b_split), 2)]
location_


# In[13]:


#  new column names to include the following set of lists
# location_, price_, review_count, reviews_, restaurant_name


# In[14]:


yelp_reviews = pd.DataFrame(list(zip(location_, price_, review_count, reviews_, restaurant_name)), columns = ['City',                 'Price_Range', 'Number_of_Reviews', 'Rating', 'Restaurant_Name'])
yelp_reviews.sample(8)


# In[15]:


yelp_reviews['Rating'] = yelp_reviews['Rating'].astype(float)
yelp_reviews


# In[16]:


yelp_reviews['Price_Value'] = yelp_reviews.apply(lambda row: len(row.Price_Range),axis=1)


# In[17]:


# yelp_reviews
yelp_reviews.columns = ['City', 'Price_Range', 'Number_of_Reviews', 'Rating', 'Restaurant_Name','Price_Value']


# In[18]:


# $= under $10. $$=11-30. $$$=31-60. $$$$= over $61.

# yelp_reviews.loc['Price_Description'] = yelp_reviews['Price_Value']
yelp_reviews.loc[yelp_reviews['Price_Value'] ==1, "Price_Description"] = "under 10"
yelp_reviews.loc[yelp_reviews['Price_Value'] ==2, "Price_Description"] = "11 - 30"
yelp_reviews.loc[yelp_reviews['Price_Value'] ==3, "Price_Description"] = "31 - 60"
yelp_reviews.loc[yelp_reviews['Price_Value'] ==4, "Price_Description"] = "over 61"
yelp_reviews.sample(10)


# In[19]:


yelp_reviews.columns = ['City', 'Price_Range', 'Number_of_Reviews', 'Rating', 'Restaurant_Name','Price_Value', 'Price_Description']


# In[20]:


yelp_reviews.columns


# In[27]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[22]:


yelp_reviews.sample(2)


# In[23]:


yelp_reviews.columns


# In[24]:


mean_std_score = yelp_reviews.groupby('City').mean()[["Rating"]]
mean_std_score['std'] = yelp_reviews.groupby('City').std()[["Rating"]]
mean_std_score.columns


# In[25]:


mean_std_score.columns = ['Mean', 'Standard Deviation']
mean_std_score.sort_values(by=['Mean'], ascending = False)


# In[28]:


# Plot to compare the average rating of restaurants in each city
plt.figure(figsize=(20,12))
# sns.set(font_scale=1.5)
fig1 = sns.violinplot(x = "City", y = "Rating", data=yelp_reviews, title = 'Comparing Average Ratings for Potential Cities').set_title('Comparing Average Yelp Ratings for Italian Restaurants in Potential Cities')

# xlabel = "Potential Cities", ylabel="Rating Distrubtion"


# In[29]:


# Plot to compare the average rating of high-end restaurants in each city
fancy_restaurants = yelp_reviews[yelp_reviews['Price_Value']>2]
fancy_restaurants.sample(80)
plt.figure(figsize=(20,12))
sns.set(font_scale=1.5)
fig1 = sns.violinplot(x = "City", y = "Rating", data=fancy_restaurants, title = 'Comparing Average Ratings # for Potential Cities').set_title('Comparing Average Yelp Ratings for High-End Italian Restaurants in Potential Cities')


# In[30]:


yelp_reviews['Number_of_Reviews'] = yelp_reviews['Number_of_Reviews'].astype(float)


# In[31]:


fancy_restaurants = yelp_reviews[yelp_reviews['Price_Value']==2]
round(fancy_restaurants.groupby('City').count()[["Number_of_Reviews"]]/yelp_reviews.groupby('City').count()[["Number_of_Reviews"]],2)


# In[32]:


fancy_restaurants = yelp_reviews[yelp_reviews['Price_Value']>2]
round(fancy_restaurants.groupby('City').count()[["Number_of_Reviews"]]/yelp_reviews.groupby('City').count()[["Number_of_Reviews"]],2)


# In[33]:


fancy_restaurants = yelp_reviews[yelp_reviews['Price_Value']==2]
round(fancy_restaurants.groupby('City').count()[["Number_of_Reviews"]]/yelp_reviews.groupby('City').count()[["Number_of_Reviews"]],2)


# In[34]:


# yelp_reviews.columns = ['City', 'Price_Range', 'Number_of_Reviews', 'Rating', 'Restaurant_Name','Price_Value', 'Price_Description']


# In[35]:


# fancy_restaurants = yelp_reviews[yelp_reviews['price_range_m']>2]
# fancy_restaurants.sample(80)
plt.figure(figsize=(16,10))
sns.set(font_scale=1.5)
fig1 = sns.violinplot(x = "City", y = "Price_Value", data=yelp_reviews, title = 'Comparing Average Ratings # for Potential Cities').set_title('Distribution of the Pricing of Italian Restaurants')

# # xlabel = "Potential Cities", ylabel="Rating Distrubtion"


# In[36]:


high_frequency = yelp_reviews[yelp_reviews['Number_of_Reviews']>450]
# high_frequency.sample(80)
plt.figure(figsize=(16,10))
sns.set(font_scale=1.5)
fig1 = sns.violinplot(x = "City", y = "Price_Value", data=high_frequency).set_title('Distribution of the Pricing of High-Frequency Italian Restaurants')

# # xlabel = "Potential Cities", ylabel="Rating Distrubtion"


# In[37]:


yelp_reviews.groupby('City').std()[["Rating"]]


# In[38]:


yelp_reviews.groupby('City').mean()[["Number_of_Reviews"]]
yelp_reviews.groupby('City').std()[["Number_of_Reviews"]]


# In[39]:


#  x for price value
#  y for rating
# group by city (hue)

plt.figure(figsize=(20,12))
sns.set(font_scale=1.1)
sns.barplot(x='Price_Value', y='Rating', data=yelp_reviews, hue='City').set_title('Ratings per Various Restaurant Prices in Each City')


# In[40]:


#  x for price value
#  y for rating
# group by city (hue)

plt.figure(figsize=(20,12))
sns.set(font_scale=1.1)
sns.barplot(x='Price_Value', y='Rating', data=high_frequency, hue='City').set_title('Ratings per Various High-Frequency Restaurant Prices in Each City')


# In[41]:


yelp_reviews.groupby('City').sum()[['Number_of_Reviews']].sort_values(by = 'Number_of_Reviews', ascending=False)


# In[42]:


yelp_reviews[yelp_reviews['City']=='Seattle, WA']


# In[43]:


yelp_reviews.groupby('City').mean()['Number_of_Reviews']


# In[44]:


yelp_reviews.groupby('City').sum()['Number_of_Reviews']/yelp_reviews.groupby('City').count()['Number_of_Reviews']


# In[45]:


yelp_reviews.groupby('City').sum()['Number_of_Reviews']


# In[46]:


yelp_reviews.groupby('City').count()['Number_of_Reviews']

