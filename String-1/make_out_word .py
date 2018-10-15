#!/usr/bin/env python
# coding: utf-8

# In[1]:


def make_out_word(out, word):
    return out[0:2]+word+out[-2:]
def main():
    
    print(make_out_word('<<>>', 'Yay'))
    
    print(make_out_word('<<>>', 'WooHoo'))
    
    print(make_out_word('[[]]', 'word'))

if __name__ == '__main__':
    main() 


# In[ ]:




