#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
rng = np.random.default_rng()
a=np.array(["Rock", "Paper", "Scissors"])
z=rng.integers(0,2) #Generate an integer 
x=int(input("Input 0,1 or 2. 0=Rock,1=Paper,2=Scissors:"))
print(f"Computer:{a[z]}")
print(f"You: {a[x]}")
print()
if x==0:
    if z==0:
        print("Draw")
    elif z==1:
        print("Computer wins")
    else:
        print("You win")
if x==1:
    if z==0:
        print("You win")
    elif z==1:
        print("Draw")
    else:
        print("Computer wins")
if x==2:
    if z==0:
        print("Computer wins")
    elif z==1:
        print("You win")
    else:
        print("Draw")

