#!/usr/bin/env python
# coding: utf-8

# In[28]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import webbrowser
from ipywidgets import interact

hphp=["https://www.youtube.com/watch?v=LQzlY60VQzI","https://www.youtube.com/watch?v=SfehQq0wC84","https://www.youtube.com/watch?v=VR2sfNabfC8",'https://www.youtube.com/watch?v=GcGrqV6e5jI','https://www.youtube.com/watch?v=Q6ki1V8CrrU','https://www.youtube.com/watch?v=tWWo_W1VGIo']
scypher=['https://www.youtube.com/watch?v=3xYinsVoSUc','https://www.youtube.com/watch?v=cuPEW9TTh2k','https://www.youtube.com/watch?v=Uof_GFjP_aw','https://www.youtube.com/watch?v=8OHn2MyszW8']
kpop=["https://www.youtube.com/watch?v=nUOeg1LYF7Y",'https://www.youtube.com/watch?v=ycYLPbtxU1Q','https://www.youtube.com/watch?v=FJ8kJdTYj1o','https://www.youtube.com/watch?v=9mQk7Evt6Vs','https://www.youtube.com/watch?v=UOxkGD8qRB4']
m1=hphp[np.random.randint(0,5)]
m2=scypher[np.random.randint(0,3)]
m3=kpop[np.random.randint(0,4)]
allmus=[m1,m2,m3]
m4=allmus[np.random.randint(0,2)]
def f(x):
    if "hiphop" in x:
        webbrowser.open(m1)
    elif "school cypher" in x:
        webbrowser.open(m2)
    elif "kpop" in x:
        webbrowser.open(m3)
    elif "隨機" in x:
        webbrowser.open(m4)

        
        
interact(f, x={"請選擇":"","hiphop":"hiphop","school cypher":"school cypher","kpop":"kpop","隨機":"隨機"});


# In[ ]:





# In[ ]:




