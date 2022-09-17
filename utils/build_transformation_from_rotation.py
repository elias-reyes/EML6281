import numpy as np

def build_transformation_from_rotation(R):
    
    P = np.array([[0,0,0]]).T
    T = np.concatenate((np.concatenate((R,P),axis=1),[[0,0,0,1]]),axis=0)

    return T