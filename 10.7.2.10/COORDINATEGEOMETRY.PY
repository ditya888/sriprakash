import numpy as np 
A = np.array([3,0])
B = np.array([4,5])
C = np.array([-1,4])
D = np.array([-2,-1])
AC = A - C
BD = B - D

Area = 0.5*np.cross(AC,BD)

print(Area)
