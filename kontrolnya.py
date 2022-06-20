#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Задача 6
def calculate(path2file):
    with open(path2file,'r', encoding='utf-8',newline='\n') as f:
        l=f.read()
        for i in l.splitlines():
            i=i.split()
            a=i[1]+i[0]+i[2]
            b=eval(a)
            print(b)
path = input('Введите путь к файлу ')


# In[4]:


#Задача 7
def substring_slice(file1,file2):
        with open(file1,'r',encoding='utf-8') as f1:
            f1=f1.read().splitlines()
            with open(file2,'r',encoding='utf-8') as f2:
                f2=f2.read().splitlines()
        lst=list(zip(f1,f2))
        for i in lst:
            text=i[0]
            num=i[1].split()
            num=[int(p) for p in num]
            print(text[num[0]:num[1]])
path1 = input('Введите путь к первому файлу ')    
path2 = input('Введите путь ко второму файлу ')   



# In[6]:


#Задача 8
import re
import json
lstel=[]
def decode_ch(string,file):
    with open(file,'rb') as f:
        data= json.load(f)    
    lst=re.sub(r'([A-Z])', r' \1', string).split()
    for i in lst:
        lstel.append(data[i])
    print(''.join(lstel))
path = input('Введите путь к json-файлу ')
string = input('Введите строку для расшифровки ') #NOTiFICaTiON

