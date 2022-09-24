from symtable import Symbol
from zipfile import PyZipFile
from sympy import * 
import numpy as np
import sys
import math as m

sys.path.append("..")
from utils import *

#init_printing( use_latex='mathjax' )  # use pretty math output

# symbolic variables px, py, pz
#var( 'px py pz' )

px = Symbol('px')
py = Symbol('py')
pz = Symbol('pz')

A_P_C0 = np.array([1, py, pz])
m_vec  = np.array([3,3,1])

A_T_B = (translate_system(A_P_C0)@build_transformation_from_axis_and_angle_of_rotation(m_vec,40))@translate_system(-A_P_C0)
#print(A_T_B)

# origin of frame B represented with symbolic variables
# equate these equations to the given point to solve for px, py, pz
# solution is not unique
print(A_T_B[:,3])

B = np.array([-2.904,2.1632,2.3319])
#A = np.array([[0.123134503621591, 0.0366445379397102, -0.479337124683902], 
#              [-0.258286644458573, 0.123134503621591, 0.405456422510948], 
#              [0.405456422510948, -0.479337124683902, 0.221642106518863]])
#
#X2 = np.linalg.solve(A,B)
eq1 = A_T_B[0,3]-B[0]
eq2 = A_T_B[1,3]-B[1]
eq3 = A_T_B[2,3]-B[2]

print(type(A_T_B[0,3]))
#print(X2)
sol = linsolve([eq3, eq1 ], (py, pz))
print(sol)