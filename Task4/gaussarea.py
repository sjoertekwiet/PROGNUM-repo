#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
A = float(input("Enter A:"))
x0 = float(input("Enter x0:"))
sig = float(input("Enter sigma:"))
z0 = float(input("Enter z0:"))
a=float(input("Enter lower limit of integration:"))
b=float(input("Enter upper limit of integration:"))
def gauss(x, A, x0, sigma, z0):
   return A*np.exp(-(x-x0)**2/(2*sig**2))+z0
func= lambda x:A*np.exp(-(x-x0)**2/(2*sig**2))+z0
X=np.linspace(-10,10,200)
y=gauss(X,A,x0,sig,z0)
x_fill=np.linspace(a,b,100)
y_fill=gauss(x_fill,A,x0,sig,z0)
I, error=sp.integrate.quad(func, a, b)
plt.plot(X,y,label=f"Area of integration = {I:.3f}")
plt.fill_between(x_fill,y_fill)
plt.legend(loc="upper left")
plt.show()
print("Integrated from 0 to2=",I,error)


# In[ ]:




