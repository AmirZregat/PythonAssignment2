#!/usr/bin/env python
# coding: utf-8

# In[1]:


def lone_sum(a, b, c):
    if a==b==c:
        return 0
    elif a==b and not a==c:
        return c
    elif not a==b and a==c:
        return b
    elif b==c and not b==a:
        return a
    else:
        return a+b+c
def main():
    
    print(lone_sum(1, 2, 3))
    
    print(lone_sum(3, 2, 3))
    
    print(lone_sum(3, 3, 3))

if __name__ == '__main__':
    main() 


# In[ ]:




