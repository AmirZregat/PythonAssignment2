#!/usr/bin/env python
# coding: utf-8

# In[1]:


def cigar_party(cigars, is_weekend):
    if is_weekend==True and cigars>=40:
        return True
    elif cigars>=40 and cigars<=60 and is_weekend==False:
        return True
    else:
        return False
def main():
    
    print(cigar_party(30, False))
    
    print(cigar_party(50, False))
    
    print(cigar_party(70, True))

if __name__ == '__main__':
    main() 


# In[ ]:




