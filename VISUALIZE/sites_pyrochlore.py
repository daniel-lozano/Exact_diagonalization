import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x=np.array([0,1,0,0,1,1,1,0,1])
y=np.array([0,1,1,0,0,1,0,1,0])
z=np.array([0,0,1,0,1,0,1,1,1])

x_i=np.array([2,2,1,2,1,2,1,1,1])
y_i=np.array([-1,0,-1,-1,0,0,0,-1,-1])
z_i=np.array([1,2,2,1,1,2,1,2,2])

translation_x=np.ones(len(x))
translation_y=np.ones(len(y))
translation_z=np.ones(len(z))

###########################################################################
############################### Lattice ##############################
###########################################################################

x_direction=np.array([1,1,-1,-1])
y_direction=np.array([1,1,1,1])
z_direction=np.array([1,-1,-1,1])

x_pos=np.array([0,1,1,0])
y_pos=np.array([0,1,0,1])
z_pos=np.array([0,0,1,1])
move=np.ones(len(x_pos))


fig=plt.figure(figsize=(7,7))
ax=fig.gca(projection='3d')
Ni=int(input("Number of tetrahedra in the x direction="))
Nj=int(input("Number of tetrahedra in the y direction="))
Nk=int(input("Number of tetrahedra in the z direction="))

points=10
x_line=np.linspace(0,Ni*2,points)
zeros=np.zeros(len(x_line))
ones=np.ones(len(x_line))
y_line=np.linspace(0,Nj*2,points)
z_line=np.linspace(0,Nk*2,points)

ans0=input("Plot lattice connections? (y) or (n):")
ans1=input("Plot nearest neighbours alpha chain? (y) or (n): ")
ans2=input("Plot nearest neighbours beta chain? (y) or (n): ")

for i in range(Ni):
    for j in range(Nj):
        for k in range(Nk):
            #            X=x+2*i+2*k
            #            Y=y+2*k
            #            Z=z+2*j+2*k
            
            X=x+translation_x*2*i
            Y=y+translation_y*2*j
            Z=z+translation_z*2*k
            
            X_I=x_i+translation_x*2*i
            Y_I=y_i+translation_y*2*j
            Z_I=z_i+translation_z*2*k
            ### Spins being added ###
            #
            ### Position of tetrahedra ###
            if((i+j)%2==0 and k%2==0):
                if(ans0=="y"):
                    ax.plot(X,Y,Z,color="gray")
                    ax.plot(X_I,Y_I,Z_I,color="gray")
                
                if(ans1=="y"):
                    ax.plot(x_line+2*i+1,-x_line+ones+2*(j+1)+1,ones+2*k,"b--",alpha=0.5,linewidth=3)
                    ax.plot(x_line+2*i+1,-x_line+ones+2*(j-1)+1,ones+2*k,"b--",alpha=0.5,linewidth=3)
                if(ans2=="y"):
                    ax.plot(x_line+2*i,x_line+2*j,zeros+2*k,"--",color="magenta",alpha=0.5)
                    ax.plot(x_line-2*i,x_line+2*j,zeros+2*k,"--",color="magenta",alpha=0.5)
        
            
            if((i+j)%2==1 and k%2==1):
                if(ans0=="y"):
                    ax.plot(X,Y,Z,color="gray")
                    ax.plot(X_I,Y_I,Z_I,color="gray")
                
                if(ans1=="y"):
                    ax.plot(x_line+2*i+1,-x_line+ones+2*(j+1)+1,ones+2*k,"b--",alpha=0.5,linewidth=3)
                    ax.plot(x_line+2*i+1,-x_line+ones+2*(j-1)+1,ones+2*k,"b--",alpha=0.5,linewidth=3)
                if(ans2=="y"):
                    ax.plot(x_line+2*i,x_line+2*j,zeros+2*k,"--",color="magenta",alpha=0.5)
                    ax.plot(x_line-2*i,x_line+2*j,zeros+2*k,"--",color="magenta",alpha=0.5)





N_max=max(max(Ni,Nj),Nk)
ans3=input("Plot directions ? (y) or (n): ")
if(ans3=="y"):
    ax.plot(x_line*N_max,x_line*N_max,x_line*N_max,"gold",linewidth=2,label="(111)")
    ax.plot(x_line*N_max,zeros,zeros,"magenta",linewidth=2,label="(100)")
    ax.plot(x_line*N_max,x_line*N_max,zeros,"blue",linewidth=2,label="(110)")
    ax.plot(x_line*N_max,x_line*N_max,x_line*N_max*2,"red",linewidth=2,label="(112)")
    plt.legend()
ax.set_title("%dX%dX%d Pyrochlore" %(Ni,Nj,Nk))
ax.set_xlim(0,2*N_max)
ax.set_ylim(0,2*N_max)
ax.set_zlim(0,2*N_max)
ax.set_xlabel("$ x $",size=20)
ax.set_ylabel("$ y $",size=20)
ax.set_zlabel("$ z $",size=20)
#plt.show()




### Tetrahedra positions ###

x=np.array ([0,1,1,0])
y=np.array ([0,1,0,1])
z=np.array ([0,0,1,1])
mu=np.array([0,1,2,3])

translation_x=np.ones(len(x))
translation_y=np.ones(len(y))
translation_z=np.ones(len(z))

###########################################################################
############################### Sites in the Lattice ######################
###########################################################################



SITES=[]
for i in range(Ni):
    for j in range(Nj):
        for k in range(Nk):

            X=x+translation_x*2*i
            Y=y+translation_y*2*j
            Z=z+translation_z*2*k
            if((i+j)%2==0 and k%2==0):
                for nu in range(len(Z)):
                    SITES.append(np.array([X[nu],Y[nu],Z[nu],mu[nu]]))
           
                ax.scatter(X,Y,Z,c=["gold","k","r","b"],s=50,alpha=1)
            
            if((i+j)%2==1 and k%2==1):
                for nu in range(len(Z)):
                    SITES.append(np.array([X[nu],Y[nu],Z[nu],mu[nu]]))
                ax.scatter(X,Y,Z,c=["gold","k","r","b"],s=50,alpha=1)

N=int(np.size(SITES)/4)
      
print("N=",N)
distance=[]

for i in range(len(SITES)):
    
    for j in range(len(SITES)):
        if(np.linalg.norm(SITES[i][:3]-SITES[j][:3])!=0):
            distance.append(np.linalg.norm((SITES[i][:3]-SITES[j][:3])))

#print(set(np.sort(distance)))

R=list(set(np.sort(distance)))
#print(R)
r1=np.sqrt(2)
r2=np.sqrt(6)
r3=np.sqrt(8)
r4=np.sqrt(10)
r5=np.sqrt(14)
r6=np.sqrt(18)
#R=[r1,r2,r3,r4,r5,r6]
R=[r1,r2,r3,r4]

#R=[r2]
ans=input("Plot interactions ? (y) or (n): ")
if(ans=="y"):
    names=["$ J_1 $","$ J_2 $","$ J_{3b} $","$ J_4 $","$ J_5 $","$ J_6 $"]
    i=0
    
    for i in range(len(R)):
        r=R[i]
    #    print(type(r))

        a=0
        for k in range(1,len(SITES)):
            if(a!=0):
                break
            

            for j in range(len(SITES)):
                
                if(np.linalg.norm(SITES[k][:3]-SITES[j][:3])!=0 and abs(np.linalg.norm((SITES[k][:3]-SITES[j][:3]))-r)<1E-2):
                    ax.plot([SITES[k][0],SITES[j][0]],[SITES[k][1],SITES[j][1]],[SITES[k][2],SITES[j][2]],linewidth=5,label=names[i])#,c=str(r/(max(R)*10)))
    #                i+=1
                    a=1

                    break
            
            if(names[i]=="$ J_{3b} $"):
               
                for j in range(len(SITES)):

                    if(np.linalg.norm(SITES[k][:3]-SITES[j][:3])!=0 and abs(np.linalg.norm((SITES[k][:3]-SITES[j][:3]))-r)<1E-2 and (SITES[k][2]-SITES[j][2])==0 ):
                        ax.plot([SITES[k][0],SITES[j][0]],[SITES[k][1],SITES[j][1]],[SITES[k][2],SITES[j][2]],linewidth=5,label="$ J_{3a} $")#,c=str(r/(max(R)*10)))
                        #                i+=1
                        a=1
                        break
    plt.legend()



#print(SITES)
N_max=max(max(Ni,Nj),Nk)

ax.set_title("%dX%dX%d Pyrochlore" %(Ni,Nj,Nk))
ax.set_xlim(0,2*N_max)
ax.set_ylim(0,2*N_max)
ax.set_zlim(0,2*N_max)
ax.set_xlabel("$ x $",size=20)
ax.set_ylabel("$ y $",size=20)
ax.set_zlabel("$ z $",size=20)
#plt.legend()
#plt.show()


BASE=3
print("Base site", SITES[2])
LIST=[]
Length=[0]
Num_steps=3

for l in range(1,Num_steps+1):
    
    current=SITES[BASE]
    steps=[BASE]
    print(steps)
    print("l=%f" %l)
    a=0
    while(len(steps)<l+1 and a==0):
        
        for i in range(len(SITES)):
            
            if( (abs(np.linalg.norm(current[:3]-SITES[i][:3])-r1) <1E-2 or
                 abs(np.linalg.norm(current[:3]-SITES[i][:3])-r2) <1E-2 or
                 abs(np.linalg.norm(current[:3]-SITES[i][:3])-r3) <1E-2) and ### 1st NN
               len(steps)!=l and ### Not the last step
               current[3]!=SITES[i][3] ): ## Not the same site
                
                current=SITES[i]
                print("  ",SITES[i])
                steps.append(i)

            elif( (abs(np.linalg.norm(current[:3]-SITES[i][:3])-r1) <1E-2 or
                   abs(np.linalg.norm(current[:3]-SITES[i][:3])-r2) <1E-2 or
                   abs(np.linalg.norm(current[:3]-SITES[i][:3])-r3) <1E-2) and
                 (SITES[i][3]==4 or SITES[i][3]==2) and ### Getting to the last site
                 current[3]!=SITES[i][3] ): ### Not the same site
                
                current=SITES[i]
                print("_",SITES[i])
                steps.append(i)
                print("len(steps)=%f" %len(steps))
                a=1
                break

    print("steps=",steps)
    if(len(steps)!=1 ):
        Length.append(len(steps))
        LIST=np.concatenate((LIST,steps)).astype(int)
        
        print("List=",LIST)



print(LIST)
print()





#### Defining the positions of the path ###
ans=input("Plot paths? (y) or (n): ")
if(ans=="y"):
    for l_index in range(1,len(Length)):
        l_init=np.sum(Length[:l_index])
        l_final=l_init+Length[l_index]
        print(l_init)
        print(LIST[l_init:l_final])

        Posx=[SITES[LIST[i]][0] for i in range(l_init,l_final)]
        Posy=[SITES[LIST[i]][1] for i in range(l_init,l_final)]
        Posz=[SITES[LIST[i]][2] for i in range(l_init,l_final)]
        ax.plot(Posx,Posy,Posz,linewidth=5)
plt.show()




