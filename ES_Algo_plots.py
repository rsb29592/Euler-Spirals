from scipy import integrate 
import matplotlib.pyplot as plt 
import numpy as np
import math as mt
import os.path as ext
import fileinput
from scipy.integrate import quad  
import pylab 

get_ipython().run_line_magic('matplotlib', 'inline')
def integrand(x,a):
    return (x**2)/(mt.sqrt(a**2-x**4))
a1 = float(input("Please inter an integer:"))
a2 = float(input("Please inter an integer:"))
a3 = float(input("Please inter an integer:"))
Array1 = np.linspace(-mt.sqrt(a1),mt.sqrt(a1),100)
y1 =[float(integrand(i,a1)) for i in Array1]
y2 =[float(integrand(i,a2)) for i in Array1]
y3 =[float(integrand(i,a3)) for i in Array1]
Array2 = [quad(integrand,0,x,args=a1) for x in Array1]
Array3 = [quad(integrand,0,x,args=a2) for x in Array1]
Array4 = [quad(integrand,0,x,args=a3) for x in Array1]


# Figure 1
plt.xlabel("x-axis", fontsize=14) 
plt.ylabel("$f(x) = \dfrac{x^2}{\sqrt{a^2-x^4}}$", fontsize=14) 
plt.title("Graph of Bernollies differentiable equation")
plt.grid()
plt.plot(Array1,y1,Array1,y2,Array1,y3, c= 'black')
fig1 = plt.gcf()
fig1.savefig("fig1_493.jpeg") 

# Figure 2
plt.xlabel("x-axis", fontsize=14) 
plt.ylabel("$F(x) = \int_{}^{}{f(x)}$", fontsize=14) 
plt.title("Graph of solutions to ODE")
plt.grid()
plt.plot(Array1,Array2,Array1,Array3,Array1,Array4, c= 'black')
fig2 = plt.gcf()
fig2.savefig("fig2_493.jpeg")
# add try statement lst to the program 


# Figure 3
a = 1
def function1(s,a):
    theta = s**2/(2*a**2)
    return mt.sin(theta)
def function2(s,a):
    theta = s**2/(2*a**2)
    return mt.cos(theta)
sparray = np.linspace(-10,10,1000)
xcordinate =  [quad(function1,0,x,args=a) for x in sparray]
ycordinate =  [quad(function2,0,x,args=a) for x in sparray]
plt.xlabel("", fontsize=14) 
plt.grid()
plt.title("Euler's' solution to the Elastica problem")
plt.plot(ycordinate , xcordinate, c= 'black')
fig3 = plt.gcf()
fig3.savefig("fig3_493.jpeg")

#Figure 4
a = 1
def function5(s,a):
    theta = s**2/(2*a**2)
    return mt.sin(theta)**2
def function6(s,a):
    theta = s**2/(2*a**2)
    return mt.cos(theta)
sparray3 = np.linspace(-10,10,1000)
xcordinate =  [quad(function5,0,x,args=a) for x in sparray3]
ycordinate =  [quad(function6,0,x,args=a) for x in sparray3]
plt.xlabel("", fontsize=14) 
plt.grid()
plt.title("Squaring one coordinate of the Euler Spiral")
plt.plot(ycordinate , xcordinate, c= 'black')
fig4 = plt.gcf()
fig4.savefig("fig4_493.jpeg")


# Figure 5
a = 1
def function5(s,a):
    theta = s**2/(2*a**2)
    return mt.sin(theta)**3
def function6(s,a):
    theta = s**2/(2*a**2)
    return mt.cos(theta)
sparray4 = np.linspace(-10,10,1000)
xcordinate =  [quad(function5,0,x,args=a) for x in sparray4]
ycordinate =  [quad(function6,0,x,args=a) for x in sparray4]
plt.xlabel("", fontsize=14) 
plt.grid()
plt.title("Cubing one coordinate of the Euler Spiral")
plt.plot(ycordinate , xcordinate, c= 'black')
fig5 = plt.gcf()
fig5.savefig("fig5_493.jpeg")

