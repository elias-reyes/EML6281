from math import sqrt
import numpy as np
from numpy import rad2deg, pi
import math

def solve_trig(A, B, D):
    
    valid   = 0
    theta_a = 0
    theta_b = 0
    sin_gamma = B / sqrt(A*A + B*B)
    cos_gamma = A / sqrt(A*A + B*B)

    gamma           = math.atan2(sin_gamma,cos_gamma)
    ratio = -D/sqrt(A*A + B*B)

    if ratio >= -1.0 and ratio <= 1.0:
        valid = 1
        cos_minus_gamma = math.acos(ratio)
        theta_a =  cos_minus_gamma + gamma
        theta_b = -cos_minus_gamma + gamma
    
    return valid, theta_a, theta_b
