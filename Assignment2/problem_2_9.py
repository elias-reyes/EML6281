import numpy as np
from transform import *
from get_axis_and_angle import *

# first rotation
A_R_C = determine_transformation_about_vector([1,0,0],35)
#print(A_R_C)

# second rotation
C_R_B = determine_transformation_about_vector([0,1,0],120)

# rotation from B to A
A_R_B = A_R_C@C_R_B

# rotation from A to B
B_R_A = A_R_B.transpose()
print(B_R_A)

m, theta =  get_axis_and_angle(B_R_A)

print(m)
print(theta)