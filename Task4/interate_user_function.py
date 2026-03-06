#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from numpy import sin, cos, exp, pi
import scipy as sp
z = input("Enter a function f(x)=")
try:
    func=lambda x:eval(z)
    I,error=sp.integrate.quad(func,0,np.pi)
    print(f"Integral (quad) = {I} +/- {error}")
    a=np.random.uniform(0,np.pi,100000)
    b=np.array([eval(z) for x in a])
    d=np.sum(b)
    e=((np.pi-0)/100000)*d
    print(f"Integral (Monte carlo) = {e}")
except SyntaxError:
    print("Syntax error")
except NameError as e:
    print(f"Name error: {e}")
except ZeroDivisionError:
    print("Zero division error")
except Exception as e:
    print(f"An error occured: {e}")

