#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install openpyxl


# In[492]:


#from openpyxl import load_workbook
wb = load_workbook('udemy_xlsx.xlsx')


# In[493]:


planilha = wb["udemy"]  # ou utilizar o comando "wb.active"


# In[494]:


a1 = planilha.cell(row=1, column=1) # ou planilha['A1']


# In[495]:


a1.value


# In[496]:


for linha in range(1, 7):
    desc = planilha[f'A{linha}']
    print(desc.value)


# In[497]:


len(planilha['A'])


# In[504]:


for linha in range(6, len(planilha['A']), 6):
    desc = planilha[f'A{linha}']
    print(desc.value)


# In[ ]:




