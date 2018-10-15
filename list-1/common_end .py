#!/usr/bin/env python
# coding: utf-8

# In[1]:


def common_end(a, b):
    if a[0]==b[0] or a[-1]==b[-1]:
        return True
    else:
        return False
def main():
    
    print(common_end([1, 2, 3], [7, 3]))
    
    print(common_end([1, 2, 3], [7, 3, 2]) )
    
    print(common_end([1, 2, 3], [1, 3]))

if __name__ == '__main__':
    main() 


# In[ ]:




