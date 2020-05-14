#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# http://www.pythonscraping.com/pages/page3.html
# https://www.youtube.com/watch?v=Vxl5jUltHBo


# In[4]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

paginas = set()
paginas_invalidas = set()
nova_pagina = ""

def getLinks(url_da_pagina):
    global paginas
    global paginas_invalidas
    
    try:
        if url_da_pagina not in paginas_invalidas:
            html= urlopen(url_da_pagina)
            bsObj = BeautifulSoup(html, "html.parser")
            serie_a_g6_2017 = ('.covid-19.|.covid.|.coronavírus.|.coronavirus.|.pandemia.')
            
            for link in bsObj.findAll("a", href=re.compile(serie_a_g6_2017)):
                if "href" in link.attrs:
                    if link.attrs['href'] not in paginas and link.attrs['href'] not in paginas_invalidas:
                        nova_pagina = link.attrs['href']
                        print(nova_pagina)
                        paginas.add(nova_pagina)
                        getLinks(nova_pagina)
    except:
        paginas_invalidas.add(nova_pagina)

getLinks("https://coronavirus.saude.gov.br/")


# In[ ]:




