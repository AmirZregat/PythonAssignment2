#!/usr/bin/env python
# coding: utf-8

# In[2]:


def close_far(a, b, c):
    if abs(a-b)<=1 and abs(a-c)>=2 and abs(b-c)>=2:
        return True
    elif abs(a-c)<=1 and abs (a-b)>=2 and abs(b-c)>=2:
        return True
    elif abs (b-c)<=1 and abs(b-a)>=2 and abs(a-c)>=2:
        return True
    else:
        return False

def main():
    
    print(close_far(1, 2, 10))
    
    print(close_far(1, 2, 3))
    
    print(close_far(4, 1, 3))

if __name__ == '__main__':
    main()     
  
  


# In[ ]:




