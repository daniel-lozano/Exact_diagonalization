import numpy as np
import matplotlib.pyplot as plt
from quspin.basis import spin_basis_1d
from quspin.operators import hamiltonian#, quantum_LinearOperator


L=1
W=12

N_sites=L*W
neigh=[]
### Building neighbours array ###
for i in range(L):
    for j in range(W):
        neigh.append([i*W+j,i*W+(j+1)%W])
        neigh.append([i*W+j,((i+1)%L)*W +j ])
print(neigh)

########################################################################
###Functions used in the code, Energy average and operator average ###
########################################################################
def average_energy(eigenvals,eigenvect,temp):
    
    average=0.0
    Z=0.0 #Partition function
    beta=1./temp
    
    for val,vect in zip(eigenvals,eigenvect.T):
        average+=(val)*np.exp(-val*beta)
        Z+=np.exp(-val*beta)
    
    return average/Z


def thermal_average(eigenvals,eigenvect,linear_op,temp):
    
    average=0 #Average of the linear operator
    Z=0 #Partition function
    beta=1./temp
    for val,vect in zip(eigenvals,eigenvect.T):
        
        average+=np.dot(vect.conj(),linear_op.matvec(vect))*np.exp(-val*beta)
        
        Z+=np.exp(-val*beta)
    return average/Z


########################################################################
################## Parameters for the model ############################
########################################################################

J=1.0
J_perp=float(input("Value for J_perp="))
T=np.linspace(1.,6,50)
N_Neighbours=4 #Number of first nearest neighbours

### Exact parameters ###
J_1_exact=[[J,i,j] for (i,j) in neigh]
J_1_perp=[[J_perp/2.,i,j] for (i,j) in neigh] ### the Half factor is

static_exact=[["zz",J_1_exact],["+-",J_1_perp],["-+",J_1_perp]]
dynamic=[]

### Basis is the same for both systems ###
basis=spin_basis_1d(L=N_sites,S='1/2',pauli=True)

H_exact=hamiltonian(static_exact,dynamic,basis=basis,check_herm=False, check_symm=False)

eigenvals_exact,eigenvect_exact=H_exact.eigh()

### Arrays to store the energy values ###
E_exact=np.zeros(len(T))
File=open("Energy_exact_"+str(J_perp)+".txt","w")

for i in range(len(T)):
#    if(i%5==0):
#        print("\nindex %d out of %d" %(i,len(T)))
    temp=T[i]
    ########################################################
    ########### Energy of the exact Hamiltonian ############
    ########################################################

    E_exact[i]=average_energy(eigenvals_exact,eigenvect_exact,temp)
    File.write(str(temp)+" "+str(E_exact[i]/N_sites)+"\n")
File.close()

plt.plot(T,E_exact/N_sites)
plt.xlabel("$ T/J $")
plt.ylabel("$ E/J $")
plt.show()
