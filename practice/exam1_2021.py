import numpy as np
import sys
import math as m

sys.path.append("..")
from utils import *

# Find A_T_B
# A_T_B = A_T_C * C_T_D * D_T_B

# translate to frame C with [2, 4, -5] being origin
A_P_C0 = np.array([2, 4, -5])
A_T_C  = translate_system(A_P_C0)
C_R_D  = determine_rotation_about_vector([1, 0, 0],35)
C_T_D  = build_transformation_from_rotation(C_R_D)

# point z given in the A frame
A_Pz = np.array([[5,3,5,1]]).T
A_m  = np.array([[2,3,4]]).T

# D_Pz = D_T_C * C_T_A * A_pz
# A_m  = D_T_C * C_T_A * A_m

D_T_C = get_reverse_transformation(C_T_D)
C_T_A = get_reverse_transformation(A_T_C)

D_Pz  = D_T_C@C_T_A@A_Pz

D_R_C = D_T_C[0:3,0:3]
C_R_A = C_T_A[0:3,0:3]

D_m   = D_R_C@C_R_A@A_m

# kind of a shortcut... translate, then rotate, then translate back
D_T_B = (translate_system(D_Pz)@build_transformation_from_axis_and_angle_of_rotation(D_m,75))@translate_system(-D_Pz) 

# calculate A_T_B
A_T_B = A_T_C@C_T_D@D_T_B

print(A_T_B)