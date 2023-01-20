#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import os
import json


# In[42]:


events = []
for line in open('2022-12-30-16.json', 'r'):
    events.append(json.loads(line))


# In[43]:


issue_events = [event for event in events if event['type']=='IssuesEvent']
issue_events


# In[46]:


# with open('new_push_event.json', 'w') as outfile:
#     outfile.write(json.dumps(events[1]))


# In[29]:


# with open('issue_event.json', 'w') as outfile:
#     outfile.write(json.dumps(issue_events[0]))


# In[ ]:




