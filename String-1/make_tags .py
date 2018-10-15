#!/usr/bin/env python
# coding: utf-8

# In[1]:


def make_tags(tag, word):
    return "<"+tag+">"+word+"</"+tag+">"
def main():
    
    print(make_tags('i', 'Yay') )
    
    print(make_tags('i', 'Hello'))
    
    print(make_tags('cite', 'Yay'))

if __name__ == '__main__':
    main() 


# In[ ]:




