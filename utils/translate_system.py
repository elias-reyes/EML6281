import numpy as np

def translate_system(P):

    if len(P) == 4:
        P = P[0:-1]

    if P.shape == (3,):
        P = np.array([P]).T

    idenity    = np.identity(3)
    translated = np.concatenate((np.concatenate((idenity,P),axis=1),[[0,0,0,1]]),axis=0)

    return translated