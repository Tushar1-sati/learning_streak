
import numpy as np
a1=np.array([11,22,33])
print(a1)
print(a1+3)
print(a1*3)

a2=np.array([[33,44,55],[66,77,88]])
a3=np.array([[33,44,55],[66,77,88],[99,111,123]])

print(np.arange(10,20))
print(np.zeros(10,dtype=int))
print(np.ones(10))

b1=np.array([[11,22,33],[44,55,66],[77,88,99]])
print(b1)
print(b1[2,2])
print(b1[2,[0,1]])
print(b1[1:3,1:3])

nd1=np.arange(25).reshape(5,5)
print(nd1)
