#!/usr/bin/env python
# coding: utf-8

# In[3]:


def diff21(n):
    if n<21:
        return 21-n
    else:
        return (n-21)*2
def main():
    print(diff21(19))
    print(diff21(10))
    print(diff21(21))
    
if __name__ =='__main__':
    main()     


# In[ ]:




