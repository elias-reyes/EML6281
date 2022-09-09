# Homework 1 Problem 2.8
# Elias Reyes 

from transform import *

A_P_C0 = np.array([[10,20,10]]).T
A_R_C  = np.identity(3)
A_T_C  = np.concatenate((np.concatenate((A_R_C,A_P_C0),axis=1),[[0,0,0,1]]),axis=0)
C_R_D  = determine_transformation_about_vector([1,0,0],30)
C_P_D0 = np.array([[0,0,0]]).T
C_T_D  = np.concatenate((np.concatenate((C_R_D,C_P_D0),axis=1),[[0,0,0,1]]),axis=0)
D_P_B0 = np.array([[-10,-20,-10]]).T
D_R_B = np.identity(3)
D_T_B = np.concatenate((np.concatenate((D_R_B,D_P_B0),axis=1),[[0,0,0,1]]),axis=0)
A_T_B = np.matmul(np.matmul(A_T_C,C_T_D),D_T_B)

# Calculate B_T_A
A_P_B0 = np.array([A_T_B[0:-1,-1]]).T
B_R_A  = A_T_B[0:3,0:3].transpose()

B_T_A  = np.concatenate((np.concatenate((B_R_A,-B_R_A@A_P_B0),axis=1),[[0, 0, 0, 1]]),axis=0)

# Calculate A_T_C
A_R_C   = determine_transformation_about_vector([2,4,6],60)
A_P_C02 = np.array([[0,0,0]]).T
A_T_C   = np.concatenate((np.concatenate((A_R_C,A_P_C02),axis=1),[[0, 0, 0, 1]]),axis=0)

# Calculate B_T_C
B_T_C = np.matmul(B_T_A,A_T_C)

print(B_T_C)