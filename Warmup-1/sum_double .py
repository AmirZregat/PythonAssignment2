#!/usr/bin/env python
# coding: utf-8

# In[4]:


def sum_double(a, b):
    if a==b:
        return (a+b)*2
    else:
        return a+b
def main():
    x=sum_double(1, 2)
    print(x)
    x=sum_double(3, 2)
    print(x)
    x=sum_double(2, 2)
    print(x)
    x=sum_double(-1, 0)
    print(x)
if __name__ =='__main__':
    main() 


# In[ ]:




