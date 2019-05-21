import numpy as np
import matplotlib.pyplot as plt

### Number of tetrahedra in the chain ###
N_tetra=3
N_sites=N_tetra*4

### Arrays for the neighbours in the chain, first, second and third ###
NN=[]
NN2=[]
NN3=[]

for i in range(N_sites):
    if(i%2 == 0):
        NN.append((i,(i+1)%N_sites))
        NN.append((i,(i+2)%N_sites))
        NN.append((i,(i+3)%N_sites))
    
        NN3.append((i,(i+5)%N_sites))
    else:
        NN.append((i,(i+1)%N_sites))
        NN.append((i,(i+2)%N_sites))

        NN3.append((i,(i+3)%N_sites))

    NN2.append((i,i+4))

print("Nearest Neighbours")
print(NN)

print("Second Nearest Neighbours")
print(NN2)

print("Third Nearest Neighbours")
print(NN3)

### Parameters of the model ###
J=1.0
J_perp=0.01
J2=J_perp**2
J3=J_perp**2
beta=0.5

print("first neighbours interaction")

J_1=[[J,i,j] for (i,j) in NN]
J_2=[[J2,i,j] for (i,j) in NN2]
J_3=[[J3,i,j] for (i,j) in NN3]
#
#print(J_1)
#print(J_2)
#print(J_3)


