import numpy as np 
import matplotlib.pyplot as plt
from sys import  argv

size=str(12)#argv[1]#input("Enter the size of the lattice=")
Jperp=input("Value of Jperp=")
FILE=np.loadtxt("Energy_magnetization_L"+size+"_Jperp"+Jperp +".txt")


print(FILE.shape)

T=FILE[:,0]
E=FILE[:,1]
Cv=FILE[:,2]



FILE_O=np.loadtxt("Energy_exact_"+Jperp+".txt")


T_O=FILE_O[:,0]
E_O=FILE_O[:,1]
#Cv_O=FILE_O[:,2]
#M_O=FILE_O[:,3]


print(T[np.argmax(Cv)])
plt.figure(figsize=(10,7))
plt.subplot(111)
plt.title("$ J_{\\perp}=$" + Jperp+"$J$")

plt.scatter(T,E,marker='D',label=size+"$\\times  $"+"3")
plt.scatter(T_O,E_O,marker='o',label="4x3_Exact")
#plt.ylim(min(E_O),0)
plt.ylabel(" $ E/J $")
plt.xlabel("$ T/J $")


###plt.xlabel("$ T $")
##plt.subplot(212)
##plt.plot(T,Cv,"k^-",label="$ T_c= $"+str(T[np.argmax(Cv)]))
###plt.plot(T_O,Cv_O,"r.-",label="$ T_c= $"+str(T_O[np.argmax(Cv_O)]))
#
#

##plt.ylim(0,3)
##plt.xlim(1.5,max(T))
plt.legend()
plt.show()


