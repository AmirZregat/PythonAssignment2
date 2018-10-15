#!/usr/bin/env python
# coding: utf-8

# In[1]:


def first_two(str):
    if len(str)<2 :
        return str
    else:
        return str[0:2]
def main():
    
    print(first_two('Hello'))
    
    print(first_two('abcdefg'))
    
    print(first_two('ab'))

if __name__ == '__main__':
    main() 


# In[ ]:




