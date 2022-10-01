import numpy as np
from numpy import rad2deg, pi
from math import cos
from math import sin
import math
import sys
sys.path.append("..")
from utils import *

Ptool_wrt_6 = np.array([5, 3, 7])
Ptool_wrt_F = np.array([25, 23, 24])
S6_wrt_F    = np.array([0.177, 0.884, -0.433])
a67_wrt_F   = np.array([-0.153, 0.459, 0.875])

a71, S7, S1, alpha71, theta7, gamma1 = close_loop(Ptool_wrt_6, Ptool_wrt_F, S6_wrt_F, a67_wrt_F)

print('a71: ',a71)
print('S7: ',S7)
print('S1: ',S1)
print('alpha71: ',alpha71)
print('theta7: ',theta7)
print('gamma1: ',gamma1)