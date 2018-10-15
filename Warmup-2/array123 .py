#!/usr/bin/env python
# coding: utf-8

# In[1]:


def array123(nums):
    if len(nums)<3:
        return False
    
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False

def main():
    
    print(array123([1, 1, 2, 3, 1]))
    
    print(array123([1, 1, 2, 4, 1]) )
    
    print(array123([1, 1, 2, 1, 2, 3]))

if __name__ == '__main__':
    main() 


# In[ ]:




