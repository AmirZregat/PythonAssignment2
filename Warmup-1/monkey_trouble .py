#!/usr/bin/env python
# coding: utf-8

# In[1]:


def monkey_trouble(a_smile, b_smile):
    if not a_smile and not b_smile:
        return True
    else:
        if a_smile and b_smile:
            return True
    return False

def main():
    x=monkey_trouble(True, True)
    print(x)
    x=monkey_trouble(False, False)
    print(x)
    x=monkey_trouble(True, False)
    print(x)
  

if __name__ == '__main__':
    main()  


# In[ ]:




