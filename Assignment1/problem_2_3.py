import numpy as np
from get_reverse_transformation import *
## part a - determine C_T_D
## C_T_D = C_T_A * A_T_B * B_T_D

# C_T_A is given
C_T_A = np.matrix([[np.sqrt(2.0)/2.0, np.sqrt(2.0)/2.0, 0, 0],[np.sqrt(2.0)/2.0, -np.sqrt(2)/2, 0, 0],[0, 0, -1, 10],[0, 0, 0, 1]])
# Calculate A_T_B
B_T_A  = np.matrix([[np.sqrt(3.0)/2.0, 0, 0.5, 20],[0 , -1, 0, 0],[0.5, 0, -np.sqrt(3)/2, 0],[0, 0, 0, 1]])
#B_P_A0 = B_T_A[0:-1,-1]
#A_R_B  = B_T_A[0:3,0:3].transpose()
#A_T_B  = np.concatenate((np.concatenate((A_R_B,-A_R_B*B_P_A0),axis=1),[[0, 0, 0, 1]]),axis=0)
A_T_B = get_reverse_transformation(B_T_A)
# Calculate B_T_D
D_T_B = np.matrix([[1, 0, 0, 0],[0, np.sqrt(3.0)/2, 0.5, 10],[0, -0.5, np.sqrt(3.0)/2, 0],[0, 0, 0, 1]])
D_P_B0 = D_T_B[0:-1,-1]
B_R_D  = D_T_B[0:3,0:3].transpose()
B_T_D  = np.concatenate((np.concatenate((B_R_D,-B_R_D*D_P_B0),axis=1),[[0, 0, 0, 1]]),axis=0)

#print(A_T_B)
#print(B_T_D)
#print(C_T_A)

# Calculate C_T_D
C_T_D = np.matmul(np.matmul(C_T_A, A_T_B), B_T_D)
print('Transformation C_T_D:')
print(C_T_D)

## part b 
D_P1 = np.matrix([20,-30,5,1]).transpose() # given coordinate, add 1 
A_P1 = np.matmul(np.matmul(A_T_B,B_T_D),D_P1)
B_P1 = np.matmul(B_T_D,D_P1)
C_P1 = np.matmul(C_T_D,D_P1)
#
print('Coordinates of point 1 measured in A:')
print(A_P1)
print('Coordinates of point 1 measured in B:')
print(B_P1)
print('Coordinates of point 1 measured in C:')
print(C_P1)