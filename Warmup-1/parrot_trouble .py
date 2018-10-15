#!/usr/bin/env python
# coding: utf-8

# In[1]:


def parrot_trouble(talking, hour):
    return (talking and (hour < 7 or hour > 20))
def main():
    
    print(parrot_trouble(True, 6))
    
    print(parrot_trouble(True, 7))
    
    print(parrot_trouble(False, 6))

if __name__ == '__main__':
    main() 


# In[ ]:




