import sys
sys.path.append("..")
from utils import *

A = 1.2
B = -5.1
D = 0.8

valid, theta_a, theta_b = solve_trig(A, B, D)

print(valid)
print(theta_a)
print(theta_b)