#!/usr/bin/env python
# coding: utf-8

# ## Deprecated since version 2.6: The urlopen() function has been removed in Python 3 in favor of urllib2.urlopen().

# Importação da função urlopen do módulo request que pertence à biblioteca [urllib]('https://docs.python.org/3.0/library/urllib.request.html')

# In[1]:


from urllib.request import urlopen


# Exibição do código HTML retornado pelo servidor web:

# In[2]:


html = urlopen("https://evaldowolkers.wordpress.com/")
print(html.read())


# Exibição das informações da página:

# In[10]:


ws = urlopen("https://github.com/andrelmfsantos/web_scrapping")
print(ws.info())

