#!/usr/bin/env python
# coding: utf-8

# In[1]:


def no_teen_sum(a, b, c):
    return fix_teen(a)+fix_teen(b)+fix_teen(c)
def fix_teen(n):
    if n>=13 and n<=19 and n!=15 and n!=16:
        return 0
    else :
        return n  
def main():
    
    print(no_teen_sum(1, 2, 3))
    
    print(no_teen_sum(2, 13, 1))
    
    print(no_teen_sum(2, 1, 14))

if __name__ == '__main__':
    main()     


# In[ ]:




