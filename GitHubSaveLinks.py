#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import time
import pandas as pd


# In[2]:


#ЧТОБЫ ВЫТАЩИТЬ ТОПИКИ ИЗ GITHUB API

# featured_topics = []
# topics_resp = requests.get('https://api.github.com/search/topics?q=is:featured')
# json_resp = topics_resp.json()
# for i in range(len(json_resp['items'])):
#   featured_topics.append(json_resp['items'][i]['name'])
# number_of_pages = (json_resp['total_count'] - len(json_resp['items']))//30+(json_resp['total_count'] - len(json_resp['items']))%30//10
# for i in range(number_of_pages):
#   time.sleep(15)
#   topics_response = requests.get('https://api.github.com/search/topics?q=is:featured&page={}'.format(i+2))
#   if topics_response.status_code == 200:
#     for j in range(len(topics_response.json()['items'])):
#       featured_topics.append(topics_response.json()['items'][j]['name'])

# pd.DataFrame(set(featured_topics), columns=['topic']).to_csv('featured_topics.csv', index=False)


# In[3]:


topics = pd.read_csv('/home/user/Downloads/featured_topics.csv')['topic']


# In[4]:


for topic in topics:
    first_response = requests.get("https://api.github.com/search/repositories?q=topic:{}&per_page=100".format(topic))
    if first_response.status_code == 200:
        pd.DataFrame(set([item['clone_url'] for item in first_response.json()['items']])).to_csv('git_links.csv', mode='a', header=False, index=False)
        for i in range(10):
            time.sleep(10)
            further_response = requests.get("https://api.github.com/search/repositories?q=topic:{}&per_page=100&page={}".format(topic,i+1))
            if further_response.status_code == 200:
                pd.DataFrame(set([item['clone_url'] for item in further_response.json()['items']])).to_csv('git_links.csv', mode='a', header=False, index=False)


# In[ ]:




