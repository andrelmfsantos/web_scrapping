#!/usr/bin/env python
# coding: utf-8

# # Módulo "re"

# ## Encontrar palavras fixas
# * [pythex: site para testas expressões regulares](https://pythex.org) 
# * [regex101: site para testas expressões regulares](https://regex101.com/#python) 

# In[1]:


import re


# In[2]:


texto = ("Esta é uma aula de Python. Esta aula é sobre Expressões Regulares. "
         "Espero que goste desta aula.")


# In[3]:


resultado = re.search("Esta", texto) # importa a primeira ocorrência encontrada
print(resultado)


# In[5]:


padrao = "Abacate" # variável padrão


# In[6]:


resultado1 = re.search(padrao, texto) # importa a primeira ocorrência encontrada
print(resultado1)


# In[7]:


if resultado1:
    print(resultado1.group())
else:
    print("Não encontrado")


# ## Caracteres especiais

# In[10]:


# "\n" caracter de enter
texto2 = ("\nEsta é uma aula de Python. Esta aula é sobre Expressões Regulares. "
         "Espero que goste desta aula.")


# In[11]:


padrao2 = "."


# In[13]:


resultado2 = re.search(padrao2, texto2)


# In[14]:


if resultado2:
    print(resultado2.group())
else:
    print("Não encontrado")


# In[17]:


resultado3 = re.search(padrao2, texto2, re.DOTALL) # encontra o caracter de entre


# In[18]:


if resultado3:
    print(resultado3.group())
else:
    print("Não encontrado")


# ### Para identificar no início do texto que comece com um determinado padrão "^"

# In[22]:


texto4 = ("Esta é uma aula de Python. Esta aula é sobre Expressões Regulares. "
         "Espero que goste desta aula.")


# In[26]:


padrao4 = "^Esta"


# In[27]:


resultado4 = re.search(padrao4, texto4, re.DOTALL) # encontra o caracter de entre


# In[28]:


if resultado4:
    print(resultado4.group())
else:
    print("Não encontrado")


# ### Para identificar no fim do texto que comece com um determinado padrão "$"

# In[40]:


padrao5 = "aula.$"
# caracter de escape:
#padrao5 = "\." # considera o caracter especial como caracter literal


# In[41]:


resultado5 = re.search(padrao5, texto4, re.DOTALL) # encontra o caracter de entre


# In[42]:


if resultado5:
    print(resultado5.group())
else:
    print("Não encontrado")


# In[49]:


# Qualquer caracter dentre os listados entre colchetes
texto6 = ("Esta é uma aula de Python. Esta aula é sobre Expressões Regulares. "
         "Espero que goste desta aula.")
padrao6 = "[aáeé]" # [a-z]: retorna todas letras minúsculas do alfabeto
resultado6 = re.search(padrao6, texto6) # retorna a primeira ocorrência
if resultado6:
    print(resultado6.group())
else:
    print("Não encontrado")


# In[50]:


# retorna todas ocorrências
resultado7 = re.findall(padrao6, texto6)
print(resultado7)


# In[52]:


# "*" retorna zero ou mais ocorrências
padrao8 = "a*" # trocar "*" por "+" retorna 1 ou mais ocorrências
resultado8 = re.findall(padrao8, texto6)
print(resultado8)


# ### Principais caractereses especiais (meta-caracteres)
# * \d: Dígito. Retorna apenas números [0-9].
# * \D: Não dígito. Retorna todos caracteres que não são números [^0-9].
# * \s: Retorna qualquer caractere de espaçamento "[\t\n\r\f\v]".
# * \S: Retorna quaquer caractere que não seja de espaçamento "[^\t\n\r\f\v]".
# * \w: Retorna qualquer caractere alfanumérico ou sublinahdo "[a-zA-Z0-9_]".
# * \W: Retorna qualquer caractere que não seja alfanumérico ou sublinhado "[^a-zA-Z0-9_]".
# * Chaves "{n}":"N" ocorrências da expressão anterior.
# * Barra vertical ou pipe "|": 'Ou' lógico.
# * Parênteses "()": Delimitam um grupo de expressões.

# In[53]:


# Retorna os números com 2 digitos
texto9 = ("_Olá, esta é uma aula de Python. Esta aula é sobre Expressões Regulares. "
         "Espero que goste desta aula. aula 10, 25, 7845, -4451, -474")
padrao9 = "\d{2}"
resultado9 = re.findall(padrao9, texto9)
print(resultado9)


# In[54]:


# Retorna os números com 2 digitos
padrao9 = "(a) | (\d{2})" # retorna uma lista com uma tupla (x,y), onde x refere-se a (a) e (y) a \d{2}
resultado9 = re.findall(padrao9, texto9)
print(resultado9)


# As funções do módulo **re** aceitam uma string representando a expressão regular.
# Expressões regulares usam a barra invertida ('\') para indicar formas especiais ou para permitir a utilização de caracteres especiais como se fossem caracteres comuns.
# Esse comportamento conflita com o uso da ('\') no Python, que utiliza este caractere para o mesmo propósito em *strings* literais. Como exemplo, temos o "\b" que é o caractere ASCII backspace)
# Para resolver este conflito, recomenda-se prefixar a stringcom r'...' para indicar uma *raw string* (*string* crua), evitando estes conflitos entre as sequências de escape de Python.

# In[58]:


# Exemplo 1
print('nOlá \bMundo')
print(r'nOlá \bMundo')


# In[59]:


# Exemplo 2
print('Expressões \b\b\b Regulares')
print(r'Expressões \b\b\b Regulares')


# In[62]:


# Exemplo 3
print('C:\\Windows\\Fonts') # a primeira contra barra indica que é para imprimir a segunda contra barra
print(r'C:\Windows\Fonts')


# ## Funções do módulo re:

# In[64]:


# Função compile
texto10 = ("_Olá, esta é uma aula de Python. Esta aula é sobre Expressões Regulares. "
         "Espero que goste desta aula. aula 10, 25, 7845, -4451, -474")
padrao10 = re.compile("e", re.IGNORECASE) # ou re.compile("e")
resultado10 = re.findall(padrao10, texto10)
print(resultado10)


# ### Função verboso
# * Permite escrever expressões regulares mais agradáveis e que sejam mais legíveis, permitindo que adicione comentários. O espaço em branco dentro do padrão é ignorado, exceto quando está em uma classe de caractereses ou quando é precedido por uma barra invertida ("\"). Quando uma linha contém um # que não está em uma classe de caracteres e não esteja precedido de uma barra invertida ("\#"), ele próprio e todos caracteres até o final da linha são ignorados.

# In[68]:


# Modo verboso
# a = re.compile(r"""\d+ # Parte inteira
#                    \.  # Ponto decimal
#                    \d* # Alguns dígitos fracionário""", re.X)
# b = re.compile(r"d+\.\d*)


# In[70]:


pattern = re.compile(r"[0-9]")
texto11 = "Olá, temos números 67 espalhados 47 neste texto 14. Mas tem negativos -7 e mais -48."
re.findall(pattern, texto11)


# In[71]:


pattern = re.compile(r"[0-9]+")
re.findall(pattern, texto11)


# In[73]:


pattern = re.compile(r"(segunda|terça|quarta|quinta|sexta)-feira")
sambadotrabalhador = ("Na segunda-feira eu não vou trabalhar. Na terça-feira não vou para poder descansar. "
                      "Na quarta preciso me recuperar. Na quinta eu acordo meio-dia, não dá. Na sexta viajo pra varanear. "
                      "No sábado vou pra mangueira sambar. Domingo é descanso e não vou mesmo lá. Mas todo fim de mês chego "
                      "devagar. Porque é pagamento eu não posso faltar")
re.findall(pattern, sambadotrabalhador)


# In[76]:


pattern = re.compile('ana')
texto12 = "Anaadora ouvir chiclete com Bana, gosta de bananada e também banana, ela é irmã da Mariana."
re.findall(pattern, texto12)


# In[77]:


pattern = re.compile('ana', re.I)
re.findall(pattern, texto12)


# ### Módulo match 
# * Busca ocorrência apenas no inicio da string

# In[78]:


texto13 = ("xOlá, esta é uma aula de Python. Esta aula é sobre Expressões Regulares. "
           "Espero que goste desta aula 10, 25, 745854, -4415, 741")
padrao = re.compile("Olá")
resultado12 = re.match(padrao, texto)
if resultado6:
    print(resultado12.group())
else:
    print("Não encontrado")


# ## Localizando CPFs/CNPJs em um texto:

# * CPNJ ou CPF: ([0-9]C[\.]?[0-9]{3}[\.]?[0-9]{3}[/]?[0-9]{4}[-]?[0-9]{2})|[0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-][0-9]{2})
#     * CNPJ: ([0-9]C[\.]?[0-9]{3}[\.]?[0-9]{3}[/]?[0-9]{4}[-]?[0-9]{2})
#     * CPF: ([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-][0-9]{2})
# 
# *----------------------------------------------------------------------------------------------------------------------*
# * [0-9]{2}: encontra no texto 2 caracteres numéricos em sequência
# * [\\.]:    localiza o caracter ponto, não sendo obrigatório
# * ?:        a interrogação após o código diz que o que esta sendo buscado não é obrigatório
# * [0-9]{3}: encontra no texto 3 caracteres numéricos em sequência
# * [/]:      localiza uma barra
# * [0-9]{4}: encontra no texto 4 caracteres numéricos em sequência
# * [-]:      encontra um hífem
# * |:        boleano que irá ser utilizado para buscar CNPJs ou CPFs

# In[81]:


padrao14 = re.compile("([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})")
#padrao = re.compile("([0-9]{2}\.?[0-9]{3}\.?[0-9]{3}[/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}\.?[0-9]{3}\.?[0-9]{3}[-]?[0-9]{2})")
#padrao = re.compile("([0-9]{2}.?[0-9]{3}.?[0-9]{3}[/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}.?[0-9]{3}.?[0-9]{3}[-]?[0-9]{2})")

# CNPJ: ([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})
# CPF: ([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})

# Texto retirado do documento concurso_novo129066_a87211e5a81747267b10c00f8d836a44.pdf
# com o resultado de um concurso que pode ser localizado na internet de forma pública
texto14 = (r"""Nº INSC. CANDIDATO CARGO C P F
RELAÇÃO DE CANDIDATOS - CONCURSO PÚBLICO
42 FABIANO FINGER SANTOS ODONTOLÓGO 00045847916 !!! SEM PONTUAÇÃO
35 FERNANDA REGINA LOTTI ODONTOLÓGO 12.345.444/7777-85 !!!!FORMATO CNPJ
70 FRANCIANE GOMES ODONTOLÓGO 049.105.969-84
87 GABRIELA REBÊLO ODONTOLÓGO 066.357.219-32
82 GUILHERME AUGUSTO TREVISOL ODONTOLÓGO 070.846.319-33
36 JACKELINE DELITSCH ODONTOLÓGO 046.692.069-58
29 JOCIE GERALDO FRATTINI ODONTOLÓGO 006.464.199-60
39 JONATHAN WOLINGER DA ROCHA LOURES ODONTOLÓGO 040.613.289-56
91 JULIANA OLIVEIRA FORNARI ODONTOLÓGO 032.359.259-70
30 KEYLLA WITTMANN ODONTOLÓGO 044.480.669-59
5 LAURA CRISTINA CAZZAMALLI ODONTOLÓGO 041.365.099-52
32 LUANA PARISOTTO ODONTOLÓGO 047.646.129-41
51 LUCIANO FERNANDES VALOTA ODONTOLÓGO 948.324.806-00
9 LUCIANO MENEGAT COLOMBELLI ODONTOLÓGO 981.097.580-53
68 LUIZ EDUARDO CORREA RODRIGUEZ ODONTOLÓGO 530.428.919-68
67 LUIZ FELIPE SANTOS PEREIRA ODONTOLÓGO 06318824995 !!!!!CPF SEM MÁSCARA
44 LUIZ OMAR WEILLER ODONTOLÓGO 828.400.590-53
31 MARCOS VINICIUS PARISOTTO ODONTOLÓGO 064.390.099-31
71 MARCUS PALMA NUNES ODONTOLÓGO 042.393.449-05
75 MARIANA MATOS KOWALSKI ODONTOLÓGO 066.165.739-66
80 MARIANE VENANCIO ANDRADE PINTO ODONTOLÓGO 058.503.489-30
38 MARLON ANDRE MAZARO ODONTOLÓGO 054.416.209-94
66 MATEUS CAMPOS VENTURA ODONTOLÓGO 053.675.399-71
33 MAURICIO SANDINI FURLAN ODONTOLÓGO 050.992.079-95
63 MONICA RIZZI ODONTOLÓGO 007.927.379-38
18 NATALIA DORINI ODONTOLÓGO 047.914.709-40
8 PAULO RICARDO CORRÊA ODONTOLÓGO 923.662.369-72
XX FULANO DE TAL 12.345.678/0001-85 !!!!!UM CNPJ
""")

resultado = re.findall(padrao, texto14)
print("CPF/CNPJ localizados no texto:", resultado)


# ## Localizando E-mails em um texto:

# * Padrão: [\w.-]+@[\w.-]+
#     * \\w: caracter alfanumérico ou sublinhado [a-zA-z0-9]
#     * .:   considera o "." como literal e não como caracter especial
#     * -:   considera o "-" como literal e não como caracter especial
#     * +:   retorna uma ou mais ocorrências da expressão anterior
#     * @:   considera um caractere arroba.

# In[83]:


padrao15 = r'[\w.-]+@[\w.-]+'
texto15 = ("Meu e-mail princial é emailteste@gmail.com, mas tenho também meuemail@hotmail.com")
match = re.findall(padrao15, texto15)
print(match)


# ## E-mails: quebrando nome do domínio

# In[99]:


texto18 = (r"Meu e-mail princial é emailteste@gmail.com, mas "
           "tenho também meuemail@hotmail.com, e p qie dozer dp "
           "eval.work@algum.com.br? Este eu ainda não tenho. "
           "Que tal também o a-s@algo.com.br?")
padrao18 = re.compile(r'([\w.-]+)@([\w.-]+)')
resultado18 = re.search(padrao18, texto18)

print("resultado:         ", resultado18.group())   # exibe o primeiro e-mail encontrado no texto
print("resultado.group(): ", resultado18.group())   # exibe o primeiro e-mail encontrado no texto
print("resultado.group(1):", resultado18.group(1))  # exibe o nome de usuário do 1º e-mail encontrado no texto
print("resultado.group(2):", resultado18.group(2))  # exibe o domínio de usuário do 1º e-mail encontrado no texto

resultado19 = re.findall(r'([\w.-]+)@([\w.-]+)', texto18)  # exibe todos e-mail encontrados, quebrando em user e domínio
print(resultado19)
for email in resultado19:
    print(email)


# ## Localizando datas em um texto:
# * Padrão: \\d{2}/\\d{2}/\\d{4}
#     * \\d{x}: Dois/Quatro números
#     * /:      Barra (literal)

# In[84]:


padrao16 = re.compile(r"\d{2}/\d{2}/\d{4}")
texto16 = "Hoje é dia 26/09/2017, a data para entrega do produto era 10/09/2017, estamos com 16 dias em atraso."
print(re.findall(padrao16, texto16))


# ## Usando split para quebrar texto com base em um caracter

# In[86]:


texto = "Evaldo|Maria|Joaquim|Cirilo|Didi|Mussum|Tarzan"
print(re.split("\|", texto)) # Como "|" é um caracter especial (boleano "OU") foi necessário colocar antes o contra barra "\"


# In[ ]:




