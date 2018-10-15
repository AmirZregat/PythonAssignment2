#!/usr/bin/env python
# coding: utf-8

# In[1]:


def squirrel_play(temp, is_summer):
    if temp>=60 and temp<=90 and not is_summer:
        return True
    elif  temp>=60 and temp<=100 and  is_summer:
        return True
    else:
        return False
def main():
    
    print(squirrel_play(70, False))
    
    print(squirrel_play(95, False))
    
    print(squirrel_play(95, True))

if __name__ == '__main__':
    main() 


# In[ ]:




