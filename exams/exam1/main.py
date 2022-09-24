import numpy as np
from math import cos
from math import sin
from math import pi
import math
import sys
sys.path.append("../..")
from utils import *

# Given coordinates in fixed frame
m_wrt_F  = np.array([[-1,3,2]]).T
PA_wrt_F = np.array([[1, 0, 5,1]]).T
PE_wrt_F = np.array([[-2, 3, 1,1]]).T

# unitize m vectore
m_hat_wrt_F = m_wrt_F / np.linalg.norm(m_wrt_F)

# from free free body diagram grab theta 
theta = math.acos(0.89443)
# calculate F_z1
xf_z1 = cos(theta)
yf_z1 = sin(theta)
#
#print(xf_z1)
#print(yf_z1)

# create trnaformation between fixed and position 1
T_1toF = np.array([[-0.44721, 0, 0.89443, 10],
                  [0.89443, 0, 0.44721, -5],
                  [0, 1.0, 0, 20],
                  [0, 0, 0, 1]])

#print(T_1toF)

# get reverse transformation
T_Fto1 =  get_reverse_transformation(T_1toF)
R_Fto1 = T_Fto1[0:3,0:3]
#print(R_Fto1)

# get coordinates in position 1 frame
m_wrt_1  = R_Fto1@m_wrt_F
PA_wrt_1 = T_Fto1@PA_wrt_F
PE_wrt_1 = T_Fto1@PE_wrt_F

# T_CtoA
T_Ato1 = translate_system(PA_wrt_1)
print(T_Ato1)

