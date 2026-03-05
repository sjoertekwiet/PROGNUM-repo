#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from numpy import sin, cos, tan, log, log10

z = input("Enter a function f(x)=")
a= float(input("Enter lower bound (a):"))
b=float(input("Enter upper bound (b):"))
c = np.random.uniform(a, b, 100000)
y=np.array([eval(z) for x in c])
w=np.sum(y)
q=((b-a)/100000)*w

print(f"The integral of f(x) from a to b ={q}")

