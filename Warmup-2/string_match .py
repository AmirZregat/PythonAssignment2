#!/usr/bin/env python
# coding: utf-8

# In[1]:


def string_match(a, b):
    if len(a)<len(b):
        l=len(a)
    else:
        l=len(b)
    c=0
    for i in range (l-1):
        if a[i:i+2]==b[i:i+2]:
            c=c+1
    return c

def main():
    
    print(string_match('xxcaazz', 'xxbaaz'))
    
    print(string_match('abc', 'abc'))
    
    print(string_match('abc', 'axc'))

if __name__ == '__main__':
    main() 


# In[ ]:




