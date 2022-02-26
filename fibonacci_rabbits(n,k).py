#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fibonacci_rabbits(n,k):
    if n == 0:
        return (0)
    elif n == 1:
        return (1)
    elif n == 2:
        return (2)
    elif n > 2:
        return (fibonacci_rabbits(n-1,k) + k*fibonacci_rabbits(n-2,k))
    else:
        return (none)
