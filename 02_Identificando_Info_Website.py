#!/usr/bin/env python
# coding: utf-8

# # Identificando informações de um website

# ## 1. Biblioteca - builtwith

# **Identificando tecnologias utilizadas por um website utilizando a biblioterca builtwith**

# In[6]:


pip install builtwith


# In[2]:


import builtwith


# In[3]:


builtwith.parse('https://www.facebook.com')


# In[4]:


builtwith.parse('https://www.metodosexatos.com')


# ## 2. Biblioteca - python-whois

# **Identificando o proprietário de um Website**

# In[7]:


pip install python-whois


# In[8]:


import whois


# In[10]:


print(whois.whois('globo.com'))


# In[11]:


print(whois.whois('metodosexatos.com'))

