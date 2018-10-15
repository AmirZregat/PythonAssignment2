#!/usr/bin/env python
# coding: utf-8

# In[6]:


def count_evens(nums):
    c=0
    for i in range(len(nums)):
        if nums[i]%2==0:
            c=c+1
    return c    




def main():
    
    print(count_evens([2, 1, 2, 3, 4]) )
    
    print(count_evens([2, 2, 0]))
    
    print(count_evens([1, 3, 5]))

if __name__ == '__main__':
    main()     
  
  


# In[ ]:




