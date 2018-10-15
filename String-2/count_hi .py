#!/usr/bin/env python
# coding: utf-8

# In[4]:


def count_hi(str):
    c=0
    for i in range (len(str)-1):
        if str[i:i+2]=="hi":
            c=c+1
    return c
  


def main():
    
    print(count_hi('abc hi ho'))
    
    print(count_hi('ABChi hi'))
    
    print(count_hi('hihi'))

if __name__ == '__main__':
    main()     
  
  


# In[ ]:




