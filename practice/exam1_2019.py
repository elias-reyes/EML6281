from symtable import Symbol
from zipfile import PyZipFile
from sympy import * 
import numpy as np
import sys
import math as m
sys.path.append("..")
from utils import *

from sympy import Matrix

A_T_B = np.array([[-0.18957, -0.36712, 0.91065, 4.37685],
                  [-0.75247, 0.65013, 0.10545, 1.12155],
                  [-0.63075, -0.66525, -0.39950, -4.26749],
                  [0, 0, 0, 1]])


A_R_B = A_T_B[:3,:3]

m, theta = get_axis_and_angle(A_R_B)

print(m)
print(theta)

# create symbolic variables
px, py, pz = symbols('px py pz')

# 
B_P1 = Matrix(((px),(py),(pz),(1)))

A_P1 = A_T_B@B_P1

print(A_P1)

# create 3 equatons with 3 unkowns
eq1 = A_P1[0] - px
eq2 = A_P1[1] - py
eq3 = A_P1[2] - pz
#
print(eq1)
print(eq2)
print(eq3)

sol = linsolve([eq1.subs(px,0),eq2.subs(px,0)],(py,pz))
print(sol)
