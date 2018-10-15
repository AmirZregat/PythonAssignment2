#!/usr/bin/env python
# coding: utf-8

# In[1]:


def lucky_sum(a, b, c):
    if  a!=13 and b!=13 and c!=13:
        return a+b+c
    elif a==13:
        return 0
    elif b==13:
        return a
    else:
        return a+b
def main():
    
    print(lucky_sum(1, 2, 3))
    
    print(lucky_sum(1, 2, 13))
    
    print(lucky_sum(1, 13, 3))

if __name__ == '__main__':
    main() 


# In[ ]:




