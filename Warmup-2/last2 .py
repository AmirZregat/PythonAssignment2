#!/usr/bin/env python
# coding: utf-8

# In[1]:


def last2(str):
    if(len(str)<2):
        return 0
    x=str[-2:]
    c=0
    for i in range(len(str)-2):
        if str[i:i+2] == x:
            c = c + 1
    return c

def main():
    
    print(last2('hixxhi')) 
    print(last2('xaxxaxaxx'))
    print(last2('axxxaaxx'))

if __name__ == '__main__':
    main() 


# In[ ]:




