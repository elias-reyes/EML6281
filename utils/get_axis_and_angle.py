import math
import numpy as np

def get_axis_and_angle(R):

    # extract matrix componants
    r11 = R[0,0]
    r12 = R[0,1]
    r13 = R[0,2]
    r21 = R[1,0]
    r22 = R[1,1]
    r23 = R[1,2]
    r31 = R[2,0]
    r32 = R[2,1]
    r33 = R[2,2]
    # calculate theta
    cosTheta = (r11+r22+r33-1)/2
    print(cosTheta)
    theta    = math.acos(cosTheta)

    if r32 - r23 > 0:
        mx = math.sqrt((r11-cosTheta)/(1-cosTheta)) 
    else:
        mx = -math.sqrt((r11-cosTheta)/(1-cosTheta)) 

    if r13 - r31 > 0:
        my = math.sqrt((r22-cosTheta)/(1-cosTheta)) 
    else:
        my = -math.sqrt((r22-cosTheta)/(1-cosTheta)) 

    if r21 - r12 > 0:
        mz = math.sqrt((r33-cosTheta)/(1-cosTheta)) 
    else:
        mz = -math.sqrt((r33-cosTheta)/(1-cosTheta)) 
    
    if math.fabs(mx) > math.fabs(my):
        my = (r12+r21)/(2*mx*(1-cosTheta))
    if math.fabs(mx) > math.fabs(mz):
        my = (r13+r31)/(2*mx*(1-cosTheta))

    return [mx,my,mz], theta*180/math.pi