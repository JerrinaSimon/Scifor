#!/usr/bin/env python
# coding: utf-8
1.Create a python program to sort the given list of tuples based on integer value using alambda function.
[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli',
24936)]
# In[14]:


lst=[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli',24936)]
res=sorted(lst,key=lambda x:x[1])
print(res)

2.Write a Python Program to find the squares of all the numbers in the given list of integers using lambda and map functions.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# In[16]:


number=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_number=list(map(lambda x:x**2,number))
print(square_number)

3.Write a python program to convert the given list of integers into a tuple of strings. Use map and lambda functions
Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
# In[1]:


number=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tup_strings=tuple(map(lambda x:str(x),number))
print(tup_strings)

 4.Write a python program using reduce function to compute the product of a list containing numbers from 1 to 25.

# In[2]:


from functools import reduce
num=list(range(1,26))
prod_lst=reduce(lambda a,b:a*b,num)
print(prod_lst)

5.Write a python program to filter the numbers in a given list that are divisible by 2 and 3 [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
# In[3]:


number=[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
result=filter(lambda x:x%2==0 and x%3==0,number)
print(list(result))

6.Write a python program to find palindromes in the given list of strings using lambda and filter function. ['python', 'php', 'aba', 'radar', 'level']
# In[4]:


lst=['python', 'php', 'aba', 'radar', 'level']
palindrome_lst=list(filter(lambda x:x==x[::-1],lst))
print(palindrome_lst)


# In[ ]:




