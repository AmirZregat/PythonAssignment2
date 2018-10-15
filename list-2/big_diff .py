#!/usr/bin/env python
# coding: utf-8

# In[7]:


def big_diff(nums):
    minn=nums[0]
    maxx=nums[0]
  
    for i in range (len(nums)-1):
        minn=min(minn,min(nums[i],nums[i+1]))
        maxx=max(maxx,max(nums[i],nums[i+1]))
  
    return maxx-minn



def main():
    
    print(big_diff([10, 3, 5, 6]) )
    
    print(big_diff([7, 2, 10, 9]))
    
    print(big_diff([2, 10, 7, 2]))

if __name__ == '__main__':
    main()     
  
  


# In[ ]:




