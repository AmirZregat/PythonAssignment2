#!/usr/bin/env python
# coding: utf-8

# In[3]:


def double_char(str):
    s=""
    for i in range(len(str)):
        s=s+str[i]+str[i]
    return s


def main():
    
    print(double_char('The'))
    
    print(double_char('AAbb'))
    
    print(double_char('Hi-There'))

if __name__ == '__main__':
    main()     
  
  


# In[ ]:




