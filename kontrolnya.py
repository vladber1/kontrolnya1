#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Задача 1
def fact(x):
    if x == 1:
        return x
    else:
        return x * fact(x - 1)


# In[4]:


# Задача 2
def filter_even(li):
    a = list(filter(lambda x: x % 2 == 0, li))
    return a


# In[6]:


# Задача 3
def square(li):
    a = list(map(lambda x: x ** 2, li))
    return a


# In[7]:


# Задача 4
def bin_search(lst, n):
    a = lst.index(n)
    return a


# In[45]:


# Задача 5
def is_palindrome(string):
    res = ''
    string = string.lower()
    string1 = string.replace(' ', '')
    for i in range(len(string1) - 1, -1, -1):
        res += string1[i]
    if res == string1:
        return 'yes'
    else:
        return 'no'


# In[54]:

# Задача 6
def calculator(path2file):
    with open(path2file, 'r', encoding='utf-8', newline='\n') as f:
        l = f.read()
        for i in l.splitlines():
            i = i.split()
            a = i[1] + i[0] + i[2]
            b = eval(a)
            return b


# In[103]:


# Задача 7
def substring_slice(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1:
        f1 = f1.read().splitlines()
        with open(file2, 'r', encoding='utf-8') as f2:
            f2 = f2.read().splitlines()
    lst = list(zip(f1, f2))
    for i in lst:
        text = i[0]
        num = i[1].split()
        num = [int(p) for p in num]
        return text[num[0]:num[1]]


# In[131]:


# Задача 8


def decode_ch(string, file):
    import re
    import json
    lstel = []
    with open(file, 'rb') as f:
        data = json.load(f)
    lst = re.sub(r'([A-Z])', r' \1', string).split()
    for i in lst:
        lstel.append(data[i])
    return ''.join(lstel)}

    # In[14]:


    # Задача 9
    class Student(object):
        def __init__(self, name, surname, fullname, grades=[3, 4, 5]):
            self.name = name
            self.surname = surname
            self.fullname = fullname
            self.grades = grades

        def greeting(self):
            return 'Hello, I am Student'

        def mean_grade(self):
            sr = sum(self.grades) / len(self.grades)
            return sr

        def is_otlichnik(self):
            if self.mean_grade() > 4.5:
                return 'YES'
            else:
                return 'NO'

        def func(self, student):
            return f'{self.name}  is friends with {student.name}'

        def __str__(self):
            return self.fullname

        # Данные для ввода в класс Student('Jora', "Pumpkin", "Jora Pumpkin Fedorovich", [1,5,4,5])

# Задача 10

class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

def ten(a):
    if len(a) == 0:
        raise MyError("Вы ничего не ввели")
    else:
        print(a)
