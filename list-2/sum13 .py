#!/usr/bin/env python
# coding: utf-8

# In[9]:


def sum13(nums):
    sum=0
    if len(nums)==0:
        return 0
    else:
        for i in range (1,len(nums)):
            if  nums[i]==13 or  nums[i-1]==13:
                continue
            elif nums[i]!=13 and nums[i-1]!=13:
                sum=sum+nums[i]
    if nums[0]!=13:
        sum=sum+nums[0]
    return sum

def main():
    
    print(sum13([1, 2, 2, 1]))
    
    print(sum13([1, 1]))
    
    print(sum13([1, 2, 2, 1, 13]))

if __name__ == '__main__':
    main()     
  
  


# In[ ]:




