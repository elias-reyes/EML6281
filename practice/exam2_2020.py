import sys
sys.path.append("..")
from utils import *

A = 0.6842
B = -0.6997
D = -0.9659

valid, theta_a, theta_b = solve_trig(A, B, D)

print('Valid:',valid)
print('Theta_a:',360.0 + rad2deg(theta_a))
print('Theta_b:',360.0 + rad2deg(theta_b))

