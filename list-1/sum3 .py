#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sum3(nums):
    s=0
    for i in range (len(nums)):
        s=s+nums[i]
    return s  
def main():
    
    print(sum3([1, 2, 3]))
    
    print(sum3([5, 11, 2]))
    
    print(sum3([7, 0, 0]))

if __name__ == '__main__':
    main() 


# In[ ]:




