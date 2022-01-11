import numpy as np
import sys
np.set_printoptions(formatter={'float': '{: 0.4f}'.format})
def func(x,y):
    return np.array([[x,y,1],[(-x*x-y*y)]],dtype=object)
def GaussianElimination(A,B,pivot,showall):
    n=len(A)
    for i in range(n):
        if(pivot==True):
            j=i+1
            row=i
            while(j<n):
                if(abs(A[i,i])<abs(A[j,i])):
                    row=j
                j=j+1
            A[[i,row], :]=A[[row,i],: ]
            B[[i,row],: ]=B[[row,i],: ]
            
        #Forward Elimination
        j=i+1
        substep=1
        while(j<n):
            if(A[i,i]==0):
                print("Denominator can not be zero")
                sys.exit() 
            if(showall==True and j==i+1):
                print("Step :"+str(i+1))
            tempA=(A[j,i]/A[i,i])*A[i,:]
            tempB=(A[j,i]/A[i,i])*B[i]
            A[j,:]=A[j,:]-tempA
            B[j]=B[j]-tempB
            if(showall==True):
                print("Substep:"+str(substep))
                substep=substep+1
                print("A matrix: ")
                #print(A)
                for k in range(len(A)):
                    for l in range(len(A[k])):
                        print("{:.4f}".format(A[k][l]),end="  ")
                    print()
                print("B matrix: ")
                #print(B)
                for k in range(len(B)):
                    for l in range(len(B[k])):
                        print("{:.4f}".format(B[k][l]),end="  ")
                    print()
            j=j+1
    #Back Substitution
    res=np.zeros(n)
    res=np.array(res,dtype=float)
    for i in range((n-1),-1,-1):
        j=n-1
        temp=A[i,:]
        if(temp[i]==0):
            print("Denominator can not be zero")
            sys.exit() 
        sum=0.0
        while(j>i):
            temp[j]=temp[j]*res[j]
            sum=sum+temp[j]
            j=j-1
        res[i]=(B[i]-sum)/temp[i]
    return res


A=[]
B=[]


"""
temp=func(-2,0)
A.append(temp[0])
B.append(temp[1])
temp=func(-1,7)
A.append(temp[0])
B.append(temp[1])
temp=func(5,-1)
A.append(temp[0])
B.append(temp[1])
n=3
"""


n=int(input())
for i in range(n):
   temp=input().split(" ")
   for j in range(n):
       A.append(float(temp[j]))
for i in range(n):
   B.append(float(input()))
  

A=np.array(A,dtype=float)
A.shape=(n,n)
B=np.array(B,dtype=float)
B.shape=(n,1)
res=GaussianElimination(A, B, pivot=True, showall=True)
print("Value of a,b,c:")
for i in range(n):
    print("{:.4f}".format(res[i]))


"""
3
25 5 1 
64 8 1 
144 12 1 
106.8 
177.2 
279.2

3
0 10 -7
6 2 3
5 -1 5
3
11
9


3 
20 15 10 
-3 -2.249 7 
5 1 3 
45 
1.751 
9

"""
      


    
    
