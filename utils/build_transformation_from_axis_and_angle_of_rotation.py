import numpy as np
from numpy import square as sqr
import math
from math import sin
from math import cos

def build_transformation_from_axis_and_angle_of_rotation(m,theta):
    
    m = np.array(m)

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
  
    A_R_B = np.reshape(A_R_B,(3,3))
    P     = np.array([[0,0,0]]).T
    
    T = np.concatenate((np.concatenate((A_R_B,P),axis=1),[[0,0,0,1]]),axis=0)

    return T