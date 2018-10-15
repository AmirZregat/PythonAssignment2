#!/usr/bin/env python
# coding: utf-8

# In[1]:


def first_last6(nums):
    return nums[0]==6 or nums[-1]==6
def main():
    
    print(first_last6([1, 2, 6]))
    
    print(first_last6([6, 1, 2, 3]))
    
    print(first_last6([13, 6, 1, 2, 3]))

if __name__ == '__main__':
    main() 


# In[ ]:




