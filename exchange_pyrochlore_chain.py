import numpy as np
import matplotlib.pyplot as plt
from quspin.basis import spin_basis_1d
from quspin.operators import hamiltonian, quantum_LinearOperator

### Number of tetrahedra in the chain ###
N_tetra=2
N_sites=N_tetra*4

print("Number of tetrahedra %d" %N_tetra)
print("Number of sites %d" %N_sites)


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

    NN2.append((i,(i+4)%N_sites))

#print("Nearest Neighbours")
#print(NN)
#print("Second Nearest Neighbours")
#print(NN2)
#print("Third Nearest Neighbours")
#print(NN3)

########################################################################
###Functions used in the code, Energy average and operator average ###
########################################################################
def average_energy(eigenvals,eigenvect,beta):
    
    average=0.0
    Z=0.0 #Partition function
    
    for val,vect in zip(eigenvals,eigenvect.T):
        average+=(val)*np.exp(-val*beta)
        Z+=np.exp(-val*beta)

    return average/Z


def thermal_average(eigenvals,eigenvect,linear_op,beta):
    
    average=0 #Average of the linear operator
    Z=0 #Partition function
    for val,vect in zip(eigenvals,eigenvect.T):
        
        average+=np.dot(vect.conj(),linear_op.matvec(vect))*np.exp(-val*beta)
        
        Z+=np.exp(-val*beta)
    return average/Z



########################################################################
################## Parameters for the model ############################
########################################################################

J=1.0
J_perp=float(input("Value for J_perp="))
BETA=np.linspace(0.001,0.5,20)
N_Neighbours=5
### Exact parameters ###
J_1_exact=[[J,i,j] for (i,j) in NN]
J_1_perp=[[J_perp/2.,i,j] for (i,j) in NN] ### the Half factor is

static_exact=[["zz",J_1_exact],["+-",J_1_perp],["-+",J_1_perp]]
dynamic=[]

### Basis is the same for both systems ###
basis=spin_basis_1d(L=N_sites,S='1/2',pauli=True)

H_exact=hamiltonian(static_exact,dynamic,basis=basis,check_herm=False, check_symm=False)

eigenvals_exact,eigenvect_exact=H_exact.eigh()

### Arrays to store the energy values ###
E_exact=np.zeros(len(BETA))
E_effective=np.zeros(len(BETA))


for i in range(len(BETA)):
    if(i%5==0):
        print("\nindex %d out of %d" %(i,len(BETA)))
    beta=BETA[i]
    #    print(beta,average_energy(eigenvals_exact,eigenvect_exact,beta))
    
    ########################################################
    ########### Energy of the exact Hamiltonian ############
    ########################################################
    
    E_exact[i]=average_energy(eigenvals_exact,eigenvect_exact,beta)
    
    ########################################################
    ######### Defining temperature dependent parameters ####
    ########################################################
    
    J1=J+2*beta*J_perp**2+8*J*(J_perp*beta)**2
    J2=-(8*J*(J_perp*beta)**2)/3.
    J3=-(8*J*(J_perp*beta)**2)/3.

    J_1=[[J1,i,j] for (i,j) in NN]
    J_2=[[J2,i,j] for (i,j) in NN2]
    J_3=[[J3,i,j] for (i,j) in NN3]

    static_effective=[["zz",J_1],["zz",J_2],["zz",J_3]]
    H_effective=hamiltonian(static_effective,dynamic,basis=basis,check_herm=False, check_symm=False)
    eigenvals_effective,eigenvect_effective=H_effective.eigh()

    ### Correction term ###
    J1_correction=2*beta*J_perp**2+16*J*(J_perp*beta)**2
    J2_correction=-(16*J*(J_perp*beta)**2)/3
    J3_correction=-(16*J*(J_perp*beta)**2)/3

    J_1_correction=[[J1_correction,i,j] for (i,j) in NN]
    J_2_correction=[[J2_correction,i,j] for (i,j) in NN2]
    J_3_correction=[[J3_correction,i,j] for (i,j) in NN3]

    static_effective_correction=[["zz",J_1_correction],["zz",J_2_correction],["zz",J_3_correction]]

    dH_eff=quantum_LinearOperator(static_effective_correction, basis=basis, check_herm=False, check_symm=False)
    
    
    E_effective_val=average_energy(eigenvals_effective,eigenvect_effective,beta)+\
        thermal_average(eigenvals_effective,eigenvect_effective,dH_eff,beta)-4*beta*(J_perp**2)*N_sites*N_Neighbours
    
    if(E_effective_val.imag>1E-10):
        print("Imaginary part is too big", E_effective_val.imag)
        break

    elif(E_effective_val.imag!=0):
        print("Imaginary part ", E_effective_val.imag)

    E_effective[i]=E_effective_val.real


    
#    print(beta,average_energy(eigenvals_effective,eigenvect_effective,beta))
#    print(beta,thermal_average(eigenvals_effective,eigenvect_effective,dH_eff,beta))
print("Energy difference")
print(E_exact-E_effective)


plt.figure(figsize=(20,10))
plt.subplot(211)
plt.plot(BETA,E_exact,"o-",label="Exact value")
plt.plot(BETA,E_effective,"o-",label="Effective value")
plt.legend()
plt.ylabel("$ \\mathrm{Energy} $")
plt.title(" %d Number of tetrahedra for $J_\perp$=%f" %(N_tetra,J_perp))
plt.subplot(212)
plt.semilogy(BETA,abs((E_exact-E_effective)/E_exact),"o-")
plt.xlabel(" $ \\beta $")
plt.ylabel("$ |\\Delta E |= |\\frac{E_{exact}-E_{effetive}}{E_{exact}} |$")
plt.savefig("Energy_Jperp=%f_NT%d.pdf" %(J_perp,N_tetra))
plt.show()

plt.plot(BETA**3,E_exact-E_effective,"o-")
plt.xlabel(" $ \\beta^3 $")
plt.ylabel("$ |\\Delta E |= |E_{exact}-E_{effetive} |$")
plt.show()

plt.subplot(211)
plt.title(" %d Number of tetrahedra for $J_\perp$=%f" %(N_tetra,J_perp))
plt.plot(BETA,E_exact/BETA,"o-",label="Exact value")
plt.plot(BETA,E_effective/BETA,".-",label="Effective value")
plt.ylabel(" $ E/\\beta $")
plt.legend()

plt.subplot(212)
plt.plot(BETA,abs(E_exact-E_effective)/BETA,".-")
plt.xlabel(" $ \\beta $")
plt.ylabel("$ |\\Delta E/\\beta |= |\\frac{E_{exact}-E_{effetive}}{\\beta} | $")
#plt.title(str(abs(E_exact[0]-E_effective[0])/BETA[0]))

plt.savefig("Energy_beta_Jperp=%f_NT%d.pdf" %(J_perp,N_tetra))


plt.show()

