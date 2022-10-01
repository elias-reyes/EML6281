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

# unitize m vector
m_hat_wrt_F = m_wrt_F / np.linalg.norm(m_wrt_F)

# from free free body diagram grab theta 
theta = math.acos(0.89443)
# calculate F_z1
xf_z1 = cos(theta)
yf_z1 = sin(theta)

# create trnaformation between fixed and position 1
T_1toF = np.array([[-0.44721, 0, 0.89443, 10],
                  [0.89443, 0, 0.44721, -5],
                  [0, 1.0, 0, 20],
                  [0, 0, 0, 1]])

# get reverse transformation
T_Fto1 =  get_reverse_transformation(T_1toF)
R_Fto1 = T_Fto1[0:3,0:3]

# get coordinates in position 1 frame
m_wrt_1  = R_Fto1@m_wrt_F
PA_wrt_1 = T_Fto1@PA_wrt_F
PE_wrt_1 = T_Fto1@PE_wrt_F

# translate to a frame centered at point A
T_Ato1 = translate_system(PA_wrt_1)
# once centered at point A, need to rotate 75 degrees about m. Note: m is unitized inside function
T_BtoA = build_transformation_from_axis_and_angle_of_rotation(m_wrt_F,75)
# once rotated, need to translate 5m along unit vector m
T_CtoB = translate_system(5*m_hat_wrt_F)
# once tranlated 5 m, need to translate back to to frame 2
T_2toC = translate_system(-PA_wrt_1)
# build T_2to1
T_2to1 = T_Ato1@T_BtoA@T_CtoB@T_2toC 

# PE_wrt_2 = T_1to2 * PE_wrt_1
T_1to2 = get_reverse_transformation(T_2to1)
PE_wrt_2 = T_1to2@PE_wrt_1

print(PE_wrt_2)