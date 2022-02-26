#!/usr/bin/env python
# coding: utf-8

# In[4]:


def fibonacci_rabbits(n,k):
    if n == 1:
        return (1)
    elif n == 2:
        return (1)
    elif n >= 3:
        return (fibonacci_rabbits(n-1,k) + k*fibonacci_rabbits(n-2,k))
    else:
        return (none)
