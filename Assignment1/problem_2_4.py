# Homework 1 problem 2.4
# Elias Reyes

import numpy as np
from numpy import square as sqr
import math
from math import sin
from math import cos


def determine_transformation_about_vector(m, theta):
    # normalize the vector which is being rotated about 
    m_hat = m / np.linalg.norm(m)

    mx = m_hat[0]
    my = m_hat[1]
    mz = m_hat[2]
    # convert theta to radians
    theta = theta*math.pi/180
    # term for simplification
    v = 1 - cos(theta)
    # transformation to A from B
    A_R_B = np.array([[sqr(mx)*v + cos(theta), mx*my*v-mz*sin(theta), mx*mz*v+my*sin(theta)],
                      [mx*my*v+mz*sin(theta), sqr(my)*v + cos(theta), my*mz*v-mx*sin(theta)],
                      [mx*mz*v-my*sin(theta), my*mz*v + mx*sin(theta), sqr(mz)*v+cos(theta)]])

    return A_R_B


#A_R_B  = determine_transformation_about_vector([2,4,7],60)
A_P_C0 = np.array([[3,4,-2]]).T
A_R_C  = np.identity(3)
A_T_C  = np.concatenate((np.concatenate((A_R_C,A_P_C0),axis=1),[[0,0,0,1]]),axis=0)

C_R_D = determine_transformation_about_vector([2,4,7],60)
C_P_D0 = np.array([[0,0,0]]).T
C_T_D = np.concatenate((np.concatenate((C_R_D,C_P_D0),axis=1),[[0,0,0,1]]),axis=0)

D_P_B0 = np.array([[-3,-4,2]]).T
D_R_B = np.identity(3)
D_T_B = np.concatenate((np.concatenate((D_R_B,D_P_B0),axis=1),[[0,0,0,1]]),axis=0)

# A_T_B = A_T_C*C_T_D*D_T_B
A_T_B = np.matmul(np.matmul(A_T_C,C_T_D),D_T_B)
print(A_T_B)