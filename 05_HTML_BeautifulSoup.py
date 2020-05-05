#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen
from bs4 import BeautifulSoup


# In[10]:


html = urlopen("file:///C:/Users/andre/OneDrive/%C3%81rea%20de%20Trabalho/hello.html")


# In[11]:


bsObj = BeautifulSoup(html.read(), "html.parser")


# In[12]:


print(bsObj.h1)
print(bsObj.title)
print(bsObj.find_all("h1"))


# In[13]:


# Pegar os links da página:
for link in bsObj.find_all('a'):
    print(link)


# In[14]:


# Pegar os links da página:
for link in bsObj.find_all('a'):
    print(link.get('href'))


# In[17]:


# Teste métodos exatos - pegar os links da página:
html1 = urlopen("https://www.metodosexatos.com/")
bsObj1 = BeautifulSoup(html1.read(), "html.parser")
for link1 in bsObj1.find_all('a'):
    print(link1.get('href'))


# In[ ]:


#-------------- Tratando erros----------------------------------
# from urllib.request import urlopen
# from urllib.request import HTTPError
# html = urlopen("http://www.udemy.com")
# print(f"Html 1:{html}"")

# try:
#     html = urlopen("http://www.udemy.com/erro")
#     print(f"Html 2: ""{html}"")
# except HTTError as erro:
#           print(erro)

# try:
#     html = urlopen("http://www.dksjsost.com")
# except URLError as erro:
#           print(erro)
          
# html = urlopen("http://www.udemy.com")
#           print(f"Html 3: {html}")
#
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen("http://www.udemy.com")
# bsObj = BeautifulSoup(html.read(),"html.parser")

# try:
#     resultado = bsObj.html.ta_nao_existente
#     print(resultado)
# except AttributeError as erro:
#     print(erro)
#--------------------------------------------------------------

