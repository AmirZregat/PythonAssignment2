#!/usr/bin/env python
# coding: utf-8

# In[1]:


def same_first_last(nums):
    return len(nums)>=1 and nums[0]==nums[-1]
def main():
    
    print(same_first_last([1, 2, 3]))
    
    print(same_first_last([1, 2, 3, 1]) )
    
    print(same_first_last([1, 2, 1]))

if __name__ == '__main__':
    main() 


# In[ ]:




