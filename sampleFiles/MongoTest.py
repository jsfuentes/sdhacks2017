
# coding: utf-8

# In[1]:


from pymongo import MongoClient


# In[2]:


client = MongoClient("mongodb://admin:admin1@ds227555.mlab.com:27555/sdhacks2017")


# In[3]:


db = client.sdhacks2017


# In[4]:


collection = db.mynewcollection


# In[6]:


collection.find_one()

