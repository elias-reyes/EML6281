import numpy as np

def get_reverse_transformation(T):
    
    # setting A_T_B is arbitrary, all that matters is the input and output are correct
    A_T_B  =  np.matrix(T)
    A_P_B0 = A_T_B[0:-1,-1]
    B_R_A  = A_T_B[0:3,0:3].transpose()
    B_T_A  = np.concatenate((np.concatenate((B_R_A,-B_R_A*A_P_B0),axis=1),[[0, 0, 0, 1]]),axis=0)

    return B_T_A
    