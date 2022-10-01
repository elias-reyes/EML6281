import numpy as np
from numpy import rad2deg, pi
from math import cos
from math import sin
import math

def close_loop(Ptool_wrt_6, Ptool_wrt_F, S6_wrt_F, a67_wrt_F):
    
    S1_wrt_F      = np.array([0, 0, 1])
    S7_wrt_F      = np.cross(a67_wrt_F,S6_wrt_F)

    S7_x_S1_wrt_F = np.cross(S7_wrt_F,S1_wrt_F)

    c71           = np.dot(S7_wrt_F,S1_wrt_F)
    
    P6orig_wrt_F = Ptool_wrt_F - np.dot(Ptool_wrt_6,np.array([1, 0, 0]))*a67_wrt_F\
                               - np.cross(np.dot(Ptool_wrt_6,np.array([0, 1, 0]))*S6_wrt_F,a67_wrt_F)\
                               - np.dot(Ptool_wrt_6,np.array([0, 0, 1]))*S6_wrt_F
    if abs(c71) == 1:

        if c71 == 1:
            alpha71 = 0
        else:
            alpha71 = 180

        S7  = 0
        s71 = 0
        S1  = np.dot(-P6orig_wrt_F,S1_wrt_F)
        a71 = np.linalg.norm(-(P6orig_wrt_F+S1*S1_wrt_F))

        if a71 == 0:
            theta7  = 0
            a71_wrt_F = a67_wrt_F
            cgamma1 = np.dot(a71_wrt_F,np.array([1, 0, 0]))
            sgamma1 = np.dot(np.cross(a71_wrt_F,np.array([1, 0, 0])),S1_wrt_F)
            gamma1  = math.atan2(sgamma1,cgamma1)
        else:
            a71_wrt_F = -(P6orig_wrt_F + S1*S1_wrt_F)/a71
            c7  = np.dot(a67_wrt_F,a71_wrt_F)
            s7  = np.dot(np.cross(a67_wrt_F,a71_wrt_F),S7_wrt_F)
            theta7  = math.atan2(s7,c7)
            cgamma1 = np.dot(a71_wrt_F,np.array([1, 0, 0]))
            sgamma1 = np.dot(np.cross(a71_wrt_F,np.array([1, 0, 0])),S1_wrt_F)
            gamma1  = math.atan2(sgamma1,cgamma1)
    else:

        a71_wrt_F = S7_x_S1_wrt_F/ np.linalg.norm(S7_x_S1_wrt_F)
        S71 = np.dot(np.cross(S7_wrt_F,S1_wrt_F),a71_wrt_F)
        c7  = np.dot(a67_wrt_F,a71_wrt_F)
        s7  = np.dot(np.cross(a67_wrt_F,a71_wrt_F),S7_wrt_F)
        c71 = np.dot(S7_wrt_F,S1_wrt_F)
        s71 = np.dot(np.cross(S7_wrt_F,S1_wrt_F),a71_wrt_F)

        theta7  = math.atan2(s7,c7)
        alpha71 = math.atan2(s71,c71)
        cgamma1 = np.dot(a71_wrt_F,np.array([1, 0, 0]))
        sgamma1 = np.dot(np.cross(a71_wrt_F,np.array([1, 0, 0])),S1_wrt_F)
        gamma1  = math.atan2(sgamma1,cgamma1)

        S7  = np.dot(np.cross(S1_wrt_F,P6orig_wrt_F),a71_wrt_F)/s71
        a71 = np.dot(np.cross(P6orig_wrt_F,S1_wrt_F),S7_wrt_F)/s71
        S1  = np.dot(np.cross(P6orig_wrt_F,S7_wrt_F),a71_wrt_F)/s71

    alpha71 = rad2deg(alpha71)
    theta7  = rad2deg(theta7)
    gamma1  = rad2deg(gamma1)

    return a71, S7, S1, alpha71, theta7, gamma1