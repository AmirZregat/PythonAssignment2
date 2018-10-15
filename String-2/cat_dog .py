#!/usr/bin/env python
# coding: utf-8

# In[5]:


def cat_dog(str):
    c=0
    d=0
    for i in range(len(str)-2):
        if str[i:i+3]=="cat":
            c=c+1
        elif   str[i:i+3]=="dog":
            d=d+1
    if c==d:
        return True
    else:
        return False



def main():
    
    print(cat_dog('catdog'))
    
    print(cat_dog('catcat'))
    
    print(cat_dog('1cat1cadodog'))

if __name__ == '__main__':
    main()     
  
  


# In[ ]:




