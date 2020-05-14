#!/usr/bin/env python
# coding: utf-8

# In[4]:


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(html, "html.parser")

imagens = soup("img", {"src":re.compile("\.{2}/img/gifts/img\d*\.jpg")})

for imagem in imagens:
    print(imagem["src"])


# In[11]:


# Erro 403 porque alguns sites tratam scraping
#html = urlopen("http://www.tudogostoso.com.br")

# Conteúdo sobre user-agent:
# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers/User-Agent
# O cabeçalho de requisição User-Agent contém uma string característica
# que permite o protocolo de rede do cliente identificar o tipo de aplicação,
# sistema operacional, fornecedor do software ou versão do software do agente
# de usuário do software solicitante.
req = Request("http://www.tudogostoso.com.br", headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()

soup = BeautifulSoup(html, "html.parser")

links = soup.findAll("a", {"href":re.compile("/categorias/.*\.php")})

for link in links:
    print(link["href"])


# In[12]:


# Quero só os links do folha.uol do mês 11 de 2017, da categoria mercado
html = urlopen("https://www.folha.uol.com.br/")
soup = BeautifulSoup(html, "html.parser")
links = soup.findAll("a", {"href":re.compile(".*\.folha\.uol\.com\.br/mercado/2017/11/.*\.shtml")})

for link in links:
    print(link["href"])


# In[ ]:




